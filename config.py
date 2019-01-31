# Application settings

# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# API metadata
API_TITLE = 'MAX Image Caption Generator'
API_DESC = 'Generates captions for images using deep learning'
API_VERSION = '0.1'

# default model
MODEL_NAME = 'im2txt'
DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)
# for image models, may not be required
MODEL_INPUT_IMG_SIZE = (299, 299)
MODEL_LICENSE = 'APACHE V2'

MODEL_META_DATA = {
    'id': '{}-tensorflow'.format(MODEL_NAME.lower()),
    'name': '{} TensorFlow Model'.format(MODEL_NAME),
    'description': '{} TensorFlow model trained on MSCOCO'.format(MODEL_NAME),
    'type': 'image_captioning',
    'license': '{}'.format(MODEL_LICENSE)
}
