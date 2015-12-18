Philonous is a markup for describing machine learning reports. Philonous assumes that it is acting on data with a particular, hierarchial structure.

* comments are in `/* */`

* parameters are in parens

* certain models might be missing certain nodes. for example, not all
  classifiers provide feature importance

```
experiment
    plots
        overall-performance-by-score
            f1
            roc-auc
    model(model-id)
            model-id
            top-n-features(n)
            scores
                f1
                roc-auc
                precision-at-x-percent(x)
            confusion
                tp
                fp
                tn
                fn
            plots
                roc
                precision-recall
                precision-over-percent
                confusion-matrix
                confusion-matrix-at-x-percent(percent)
                top-n-features(n)
            test-set
                /*
                    extra columns include:
                    predicted-probability
                    predicted-labels
                */
                select(query)
                    /* Supports single select statements. FROM clause must be "FROM test" 
                       (since the target is implicit */
                    /* If a table is returned, makes an html table. If one
                       result is returned, just makes that */
            train-set
                /* extra columns include:
                   labels
                */
                select(query)
                    /* Supports single select statements. FROM clause must be "FROM train" 
                       (since the target is implicit */
                    /* If a table is returned, makes an html table. If one
                       result is returned, just makes that */
                
            metadata
                summary
                time
                classifier
                    name
                    summary
                    ...
                ...
    best-model(metric)
        /* metric can be 'f1', 'roc-auc', etc. */
        ... /* defines everything that model does */
    for-each-model(filter-by, sort-by, limit)
        /* repeats for every model in the experiment */
        /* filter_by is something like "$model.metadata.time < 2013" */
        ... /* defines everything that model does */

```

These directives are embedded in HTML. 


<div id="philoneous">
    <ph-experiment>
        <ph-plots>
            <ph-overall-performance-by-score>
                <ph-f1></ph-f1>
            </ph-overall-performance-by-score>
        </ph-plots>
        <ph-best-model>
        </ph-best-model>
