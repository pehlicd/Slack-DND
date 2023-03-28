# Slack DND 💤

Slack DND is a simple MacOS status bar application that allows you to set your Slack status to Do Not Disturb (DND) mode. 
It is useful for those who want to avoid distractions during their work hours.

## Configuration

Slack DND requires a Slack API token to work. You can get one by following the instructions below:

1. Go to https://api.slack.com
2. Create an app (or use an existing one) with selecting **from scratch** option.
3. From the sidebar, go to **OAuth & Permissions** and scroll down to the **User Token Scopes** section.
4. Give following permissions to your app:
    - `dnd:write`
    - `dnd:read`
5. Install the app to your workspace. After installation, you will see a **User OAuth Access Token**. Copy it and paste it to the Slack DND app at startup for once. (You can also change it later from the app's configuration file `$HOME/.slack-dnd/config.json`.)

## Installation

### From Releases

Run following command in your favorite terminal:

```bash
curl -sL https://github.com/pehlicd/Slack-DND/releases/download/v0.0.1/Slack.DND.tar.gz | tar -zx -C /Applications
```

### From Source Code

1. Clone the repository and navigate to the project directory.
2. Install required dependencies with `pip3 install -r requirements.txt`.
3. Run `python setup.py py2app` to build the application.
4. Copy the application to your Applications folder with `cp dist/Slack\ DND.app/Contents/MacOS/Slack\ DND  ~/Applications/Slack\ DND` command.
5. You are ready to go! Run **Slack DND** 💤

## Contribution

See [Contribution Guide](CONTRIBUTING.md).
