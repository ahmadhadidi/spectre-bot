import logging
import rasa

logging.info("attempting to run rasa")

# Make necessary bindings
# Todo: Add to .env
model_path = "./rasa_folder/models/latest.tar.gz"
model_name = "latest"
domain_path = "./rasa_folder/domain.yml"
credentials_path = "./rasa_folder/credentials.yml"
endpoints_path = "./rasa_folder/endpoints.yml"
config_path = "./rasa_folder/config.yml"
training_data_path = "./rasa_folder/data"
output_path = "./rasa_folder/models"

# Train if needed
rasa.train(domain=domain_path,
           config=config_path,
           training_files=training_data_path,
           output=output_path,
           fixed_model_name=model_name)

# Run Rasa
rasa.run(model=model_path,
         endpoints=endpoints_path,
         port=5005,
         cors="*",
         connector="rest",
         enable_api=True)
