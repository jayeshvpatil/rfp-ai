model_name='mistral:latest'
custom_model_name='mistral-jp-local'

ollama pull $model_name

ollama create $custom_model_name -f ./local_llm/mistral_modelfile