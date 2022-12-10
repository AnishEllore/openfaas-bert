# openfaas-bert
## Prerequisites
1. Install Docker. [Steps](https://docs.docker.com/get-docker/).
2. Install openfaas on a kubernetes cluster. [Steps(https://docs.openfaas.com/deployment/kubernetes/#install-the-openfaas-chart-using-arkade-or-helm).

## Deploy Bert using this git repo

**Before starting this step you should have some dummy function deployed to see if your setup is working**
```
faas-cli template store list
faas-cli template pull
update docker image name in bert.yml
./run.sh
echo "hi mmy name is bert" | faas-cli invoke bert
python3 test.py bert inputdatapath
```

## Deploy Name Classifier
```
faas-cli deploy --image=theaxer/classify:latest --name=classify
echo "Donald Trump" | faas-cli invoke classify
python3 test.py bert inputdatapath
```
