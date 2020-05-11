# OIC_start-stop
This shows how to use the OCI API to start and stop your OIC instance.

For more information on Oracle Integration, click [here](https://garyhostt.github.io/Oracle_Integration/).

## How to use

You will need to change the following lines in the code: 13, 18, 20, and 22, to have your relevant details.

In order to authenticate the API calls to OCI, we use [signing requests](https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/signingrequests.htm). If you have problems, double check your credentials, or look at the [OCI API Errors documentation](https://docs.cloud.oracle.com/en-us/iaas/Content/API/References/apierrors.htm).

This script also calls the [announcements API](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/announcements/0.0.1/).

This script is made for instances in the Ashburn region, if your's is located elsewhere, please see this [documentation](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/integration/20190131/). You will then need to change the code on lines 120, 134, and 149.
- [StartInstance endpoint](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/integration/20190131/IntegrationInstance/StartIntegrationInstance)
- [StopInstance endpoint](https://docs.cloud.oracle.com/en-us/iaas/api/#/en/integration/20190131/IntegrationInstance/StopIntegrationInstance)
