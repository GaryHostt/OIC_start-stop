# OIC_start-stop

<p align="center">
  <img src="https://github.com/GaryHostt/OIC_start-stop/blob/master/2.jpg?raw=true" alt="OIC"/>
</p>

## Introduction

This python script, [start_stop.py](https://github.com/GaryHostt/OIC_start-stop/blob/master/start_stop.py), uses the OCI API to start & stop your Oracle Integration instance, and get announcements.

For more information on Oracle Integration, click [here](https://garyhostt.github.io/Oracle_Integration/).

## How to use

First, your tenancy must have a [configured user that can call the OCI API, with an API key](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm). Next, that user needs to have the [USE permission in IAM](https://docs.oracle.com/en/cloud/paas/integration-cloud/oracle-integration-oci/iam-policy-permissions.html) for OIC.

You will need to change the following lines in the code: 13, 18, 20, and 22, to have your relevant details.

In order to authenticate the API calls to OCI, we use [signing requests](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm). If you have problems, double check your credentials, or look at the [OCI API Errors documentation](https://docs.cloud.oracle.com/en-us/iaas/Content/API/References/apierrors.htm).

This script also calls the [announcements API](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/announcements/0.0.1/).

This script is made for instances in the Ashburn region, if your instance is located elsewhere, please see this [documentation](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/integration/20190131/). You will then need to change the code on lines 120, 134, and 149.
- [StartInstance endpoint](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/integration/20190131/IntegrationInstance/StartIntegrationInstance)
- [StopInstance endpoint](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/integration/20190131/IntegrationInstance/StopIntegrationInstance)

After configuring your credentials, once you run the script, simply enter 1, 2, or 3. Then paste your relevant OCIDs.

## Where to find your tenancy OCID

![](5.jpg)
From the OCI console, click the top left hamburger menu, navigate to identity, then compartments. Click your root compartment.

![](6.jpg)
Now copy the OCID from the details screen.

## Where to find your OIC OCID

![](3.jpg)
From the OCI console, navigate to Application Integration. Click on your instance. 

![](4.jpg)
This is where you can copy your OCID that is to be inputted with the script prompt. 



