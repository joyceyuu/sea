"""Modeling for sea data."""
import numpy as np
from typing import Any
import matplotlib.pyplot as pl
import glabrezu as gl
from dretch import io, config


def main() -> Any:
    """Apply different classifiers to sea data."""
    value = io.load_modron(config.output_file)
    train_value, query_value = value['train'], value['query']

    # define transformers and model
    transformer = [gl.transforms.ScaleFloats()]
    models = {
        'Logistic': gl.Pipeline(transformer,
                                gl.classifiers.LogisticRegression())
    }

    # validation
    scores = gl.validation.ScoreAggregator()
    for name in models:
        model_scores, predictions = gl.validation.kfold(
            models[name], train_value, folds=3, random_state=0
        )
        print("##### {} #####".format(name))
        gl.validation.print_scores(model_scores)
        scores.update(name, model_scores)
        gl.vis.yyplot(predictions, train_value.Y, log=True,
                      alpha=0.1)
        pl.title(train_value.Y.ordinal_columns[0] + ' ' + name + ' R2=' +
                 str(np.mean(model_scores['R2'])))
        pl.show()
    print(scores.table())
