# openfaas-bert
## Install openfaas on a kubernetes cluster
1. Use link to install using arkade https://docs.openfaas.com/deployment/kubernetes/#install-the-openfaas-chart-using-arkade-or-helm

## Deploy Bert using this git repo
### Before starting this step you should have some dummy function deployed to see if your setup is working
1. faas-cli template store list
2. faas-cli template pull
3. update docker image name in bert.yml
4. ./run.sh
5. echo "hi mmy name is bert" | faas-cli invoke bert
6. python3 test.py bert inputdatapath

## Deploy Name Classifier
1. faas-cli deploy --image=theaxer/classify:latest --name=classify
