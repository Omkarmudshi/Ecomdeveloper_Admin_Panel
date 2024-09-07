pytest -s -v -m "regression" --html=Reports\report_regression_test_group.html testCases/
rem pytest -s -v -m "sanity" --html=Reports\report_sanity_test_group.html testCases/
rem pytest -s -v -m "sanity and regression" --html=Reports\report_sanity_and_regression_test_group.html testCases/
rem pytest -s -v -m "sanity or regression" --html=Reports\report_sanity_and_regression_test_group.html testCases/