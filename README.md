# Slack Greeter Balena Block
Send a message to Slack when your Balena device comes online

The greeter service provides a simple app that sends a message on Slack to notify when a vehicle becomes online.
It does this by posting the message using a [Slack webhook](https://api.slack.com/messaging/webhooks) that is connected to a specific Slack channel.

## Setup

First, deploy the service to your fleet.
Then to get this to work, set up a webhook by following [Slack's webhook documentation](https://api.slack.com/messaging/webhooks).
This will provide you with a URL that starts with `https://hooks.slack.com/services`.
Copy this URL, and create a [Fleet-wide Variable](https://docs.balena.io/learn/manage/variables/#fleet-wide-variables) (or a [Device Variable](https://docs.balena.io/learn/manage/variables/#device-variables) if you want to enable this only for individual vehicles) with the name `GREETER_WEBHOOK_URL`, and set the webhook URL as its value.
Select to enable the variable only for the greeter service
This should restart the service automatically and trigger a greeting in Slack.

### Further configuration

You can set the following optional environment variables to customize the application:

* `GREETER_DEVICE_NOUN` - The noun to use to refer to your devices, e.g. 'device', 'robot', 'thermostat'. Default: 'device'.
