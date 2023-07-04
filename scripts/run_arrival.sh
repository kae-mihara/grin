python ./scripts/run_imputation.py \
    --window=12  \
    --horizon=12 \
    --in-sample=false \
    --epoch=200 \
    --patience=20 \
    --dataset-name=arrival \
    --model-name=grin
