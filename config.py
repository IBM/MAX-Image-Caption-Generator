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

# Application settings

# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'MAX Image Caption Generator'
API_DESC = 'Generate captions that describe the contents of images.'
API_VERSION = '1.1.0'

# default model
MODEL_NAME = 'im2txt'
DEFAULT_MODEL_PATH = 'assets/checkpoint/model2.ckpt-2000000'
VOCAB_FILE = './assets/word_counts.txt'
# for image models, may not be required
MODEL_INPUT_IMG_SIZE = (299, 299)
MODEL_LICENSE = 'Apache 2.0'

MODEL_META_DATA = {
    'id': API_TITLE.lower().replace(' ', '-'),
    'name': API_TITLE,
    'description': '{} TensorFlow model trained on MSCOCO'.format(MODEL_NAME),
    'type': 'Image-to-Text Translation',
    'license': MODEL_LICENSE,
    'source': 'https://developer.ibm.com/exchanges/models/all/max-image-caption-generator/'
}
