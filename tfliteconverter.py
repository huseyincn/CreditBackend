import tensorflow as tf

reloaded_model = tf.keras.models.load_model('exportedModel')


# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(reloaded_model)
# converter.allow_custom_ops = True
converter.target_spec.supported_ops = [
  tf.lite.OpsSet.TFLITE_BUILTINS,  tf.lite.OpsSet.SELECT_TF_OPS
]
# converter.target_spec.experimental_select_user_tf_ops = [
#     'raw_ops.DenseBincount',
# ]

tflite_model = converter.convert()

# Save the model.
with open('exportedMMobil.tflite', 'wb') as f:
  f.write(tflite_model)


"""
BU MODEL TFLITE'A ÇEVRİLMİYOR DOLAYISIYLA MICROSERVICE BACKEND YAZIP GONDERICEZ
"""