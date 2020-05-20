import logging
import os
import tarfile

# TODO https://github.com/tensorflow/tensorflow/issues/35185
# removing these imports might cause segfault
# import tensorflow
# import sklearn
import rasa

logger = logging.getLogger(__name__)

models_directory = './rasa_folder/models'
fixed_model_name = os.getenv('AGENT_MODEL_NAME', 'latest')


def model_path() -> str:
    return os.path.join(models_directory, '{}.tar.gz'.format(fixed_model_name)).format()


def extract_tar_file(tar_path):
    tf = tarfile.open(tar_path)
    tf.extractall(path="./rasa_folder/models/test")
    return "extracted the mofo"


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.Formatter('%(name)s - %(levelname)s - %(message)s')

    if not os.path.exists(models_directory):
        logger.info("Path doesnt exist %s" % models_directory)
        os.makedirs(models_directory)

    logger.info('Training model with fixed_model_name: %s ' % fixed_model_name)
    trained_model_path = rasa.train('./rasa_folder/domain.yml',
                                    './rasa_folder/config.yml',
                                    './rasa_folder/data',
                                    output=models_directory,
                                    fixed_model_name=fixed_model_name)

    logger.info("Training model finished")

    extract_tar_file(trained_model_path)

    try:
        os.rename(trained_model_path, model_path())
    except OSError as error:
        logger.error(error)

    assert os.path.exists(model_path())
    logger.info('Model exists in: %s' % os.path.abspath(model_path()))
