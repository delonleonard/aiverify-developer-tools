from test_engine_core.plugins.enums.model_type import ModelType

from tests.plugin_test import PluginTest

if __name__ == "__main__":
    # TODO: Define data, model, ground_truth file location. Requires absolute path.
    #       Define core modules path as relative/absolute path. If you cloned the project using 
    #       the provided setup script, leave core_modules_path as an empty string.
    # Example:
    # data_path = "tests/user_defined_files/data/pickle_pandas_mock_binary_classification_credit_risk_testing.sav"
    # model_path = "tests/user_defined_files/model/binary_classification_mock_credit_risk_sklearn.linear_model._logistic.LogisticRegression.sav"
    # ground_truth = "default"
    # model_type = ModelType.CLASSIFICATION
    core_modules_path = ""
    data_path = "tests/user_defined_files/data/pickle_pandas_mock_binary_classification_credit_risk_testing.sav"
    model_path = "tests/user_defined_files/model/binary_classification_mock_credit_risk_sklearn.linear_model._logistic.LogisticRegression.sav"
    ground_truth_path = "tests/user_defined_files/data/pickle_pandas_mock_binary_classification_credit_risk_testing.sav"
    ground_truth = "default"
    model_type = ModelType.CLASSIFICATION
    run_pipeline = False

    # TODO: Define the plugin input parameters value referenced from input.schema.json
    # Example:
    # plugin_arguments_value = {
    #     "argument1": "MyArgumentValue"
    # }
    plugin_argument_values = {}

    # =====================================================================================
    # NOTE: Do not modify the code below
    # =====================================================================================
    # Perform Plugin Testing
    try:
        # Create an instance of PluginTest with defined paths and arguments and Run.
        plugin_test = PluginTest(
            run_pipeline,
            core_modules_path,
            data_path,
            model_path,
            ground_truth_path,
            ground_truth,
            model_type,
            plugin_argument_values,
        )
        plugin_test.run()

    except Exception as exception:
        print(f"Exception caught while running the plugin test: {str(exception)}")
