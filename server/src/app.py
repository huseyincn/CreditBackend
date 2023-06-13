from flask import Flask, request, make_response, jsonify
import pandas as pd
import tensorflow as tf


reloaded_model = tf.keras.models.load_model('exportedModelacc82')

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        checking_status = request.form['checking_status']
        duration = request.form['duration']
        credit_history = request.form['credit_history']
        purpose = request.form['purpose']
        credit_amount = request.form['credit_amount']
        savings_status = request.form['savings_status']
        employment = request.form['employment']
        installment_commitment = request.form['installment_commitment']
        other_parties = request.form['other_parties']
        residence_since = request.form['residence_since']
        property_magnitude = request.form['property_magnitude']
        age = request.form['age']
        other_payment_plans = request.form['other_payment_plans']
        housing = request.form['housing']
        existing_credits = request.form['existing_credits']
        job = request.form['job']
        num_dependents = request.form['num_dependents']
        own_telephone = request.form['own_telephone']
        foreign_worker = request.form['foreign_worker']
        sex = request.form['sex']
        marriage = request.form['marriage']

        data = [[checking_status, float(duration), credit_history, purpose, float(credit_amount), savings_status,
                 employment, float(installment_commitment), other_parties, float(
                     residence_since), property_magnitude,
                 float(age), other_payment_plans, housing, float(
                     existing_credits), job, float(num_dependents), own_telephone,
                 foreign_worker, sex, marriage]]

        columns = ['checking_status', 'duration', 'credit_history', 'purpose',
                   'credit_amount', 'savings_status', 'employment',
                   'installment_commitment', 'other_parties', 'residence_since',
                   'property_magnitude', 'age', 'other_payment_plans', 'housing',
                   'existing_credits', 'job', 'num_dependents', 'own_telephone',
                   'foreign_worker', 'sex', 'marriage']

        df = pd.DataFrame(data=data, columns=columns)

        ds = df_to_dataset(df, False, len(df))

        result = reloaded_model.predict(ds)

        return make_response(jsonify({"result": str(result)}))


def df_to_dataset(dataframe, shuffle=True, batch_size=32):
    df = dataframe.copy()
    df = {key: value[:, tf.newaxis] for key, value in dataframe.items()}
    ds = tf.data.Dataset.from_tensor_slices((dict(df)))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(dataframe))
    ds = ds.batch(batch_size)
    ds = ds.prefetch(batch_size)
    return ds


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
