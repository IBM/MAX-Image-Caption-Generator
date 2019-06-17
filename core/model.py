#
# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from maxfw.model import MAXModelWrapper

import math
import logging

import tensorflow as tf

from core import configuration
from core import inference_wrapper
from core.inference_utils import vocabulary
from core.inference_utils import caption_generator

from config import DEFAULT_MODEL_PATH, VOCAB_FILE

logger = logging.getLogger()


class ModelWrapper(MAXModelWrapper):

    def __init__(self, path=DEFAULT_MODEL_PATH):
        # TODO Replace this part with SavedModel
        g = tf.Graph()
        with g.as_default():
            model = inference_wrapper.InferenceWrapper()
            restore_fn = model.build_graph_from_config(configuration.ModelConfig(),
                                                       path)
        g.finalize()
        self.model = model
        sess = tf.Session(graph=g)
        # Load the model from checkpoint.
        restore_fn(sess)
        self.sess = sess

    def _predict(self, image_data):
        # Create the vocabulary.
        vocab = vocabulary.Vocabulary(VOCAB_FILE)

        # Prepare the caption generator. Here we are implicitly using the default
        # beam search parameters. See caption_generator.py for a description of the
        # available beam search parameters.
        generator = caption_generator.CaptionGenerator(self.model, vocab)

        captions = generator.beam_search(self.sess, image_data)

        results = []
        for i, caption in enumerate(captions):
            # Ignore begin and end words.
            sentence = [vocab.id_to_word(w) for w in caption.sentence[1:-1]]
            sentence = " ".join(sentence)
            # print("  %d) %s (p=%f)" % (i, sentence, math.exp(caption.logprob)))
            results.append((i, sentence, math.exp(caption.logprob)))

        return results
