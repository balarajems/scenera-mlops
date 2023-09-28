
## create resource group
```az group create --name scenera-secure-az-ml --location eastus```

## Create the virtual Network
```
az network vnet create \
    --name scenera-vnet \
    --resource-group scenera-secure-az-ml \
    --address-prefix 10.0.0.0/16 
```

## Create the training Subnet (Compute instances etc)
```
az network vnet subnet create --name scenera-subnet-training \
                              --resource-group scenera-secure-az-ml \
                              --vnet-name scenera-vnet \
                              --address-prefixes 10.0.0.0/24
```

## Create the Secoring Subnet
```
az network vnet subnet create --name scenera-subnet-scoring \
                              --resource-group scenera-secure-az-ml \
                              --vnet-name scenera-vnet \
                              --address-prefixes 10.0.1.0/24
```

## Create the Bastion Subnet 
```
az network vnet subnet create --name AzureBastionSubnet \
                              --resource-group scenera-secure-az-ml \
                              --vnet-name scenera-vnet \
                              --address-prefixes 10.0.254.0/26
```

## Create the Gateway Subnet 
```
az network vnet subnet create --name GatewaySubnet \
                              --resource-group scenera-secure-az-ml \
                              --vnet-name scenera-vnet \
                              --address-prefixes 10.0.250.0/24
```

## Create the Firwall Subnet 
```
az network vnet subnet create --name AzureFirewallSubnet \
                              --resource-group scenera-secure-az-ml \
                              --vnet-name scenera-vnet \
                              --address-prefixes 10.0.252.0/26
```

## Create the private endpoint Subnet 
```
az network vnet subnet create --name scenera-subnet-private-endpoint \
                              --resource-group scenera-secure-az-ml \
                              --vnet-name scenera-vnet \
                              --address-prefixes 10.0.2.0/24
```

##  Provision of the Azure Machine Learning Service
 create Azure Machine Learning Service from the portal

## Create the private link endpoint for the other services
Create the private link endpoint for all services using same subnet as the AzualML
 

### reference
 ```https://techcommunity.microsoft.com/t5/fasttrack-for-azure/secure-azure-machine-learning-service-azureml-environment/ba-p/3162297```