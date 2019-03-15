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
