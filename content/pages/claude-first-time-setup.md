Title:   Claude Code 
Date:    07/28/2026
Authors: Sean Eddy
slug:    claude-first-time-setup

These notes tell you how to install Claude Code under Harvard's
official auspices, and have it direct bill to our lab funding.

## 1. Install Claude Code.

Go to [claude.com/download](https://claude.com/download)
and follow the instructions.

You won't be able to run it yet. You need an API key. That's next.



## 2. Apply to HUIT for your "app" API key.

Go to:
[portal.apis.huit.harvard.edu/register-an-app](https://portal.apis.huit.harvard.edu/register-an-app).

Sign in to Harvard Key at the upper right.

Your username in the upper right is a drop-down menu; select `Apps`.

Press the `+ NEW APP` button in the upper right.
  
Provide the following information to the form:

  - App name:  `<LastName>_FAS`  
    Example for me: `Eddy_FAS`

  - Description: `<YourName> - FAS faculty fund - HUIT customer B40802 - monthly limit $400`  
    Example for me: `Sean Eddy - FAS faculty fund - HUIT customer B40802 - monthly limit $400`
    
  - Owner: select `me <your_email_address>`  
    Example for me: `me <seaneddy@fas.harvard.edu>`
    
  - APIs: select `AI Services - AWS Bedrock API` by pressing the
    Request button.
    
When done, click the `SAVE` button in the lower right. 
  
Approval is automatic, if HUIT's script sees our valid HUIT customer
number.
  
This sets up monthly billing to the lab's startup fund. Our startup
fund is a nigh-nonrenewable resource right now. Use it wisely. The
HUIT script is supposed to see the $400 monthly limit and honor it,
but I'm not yet sure that it does. I have been tracking my Claude
session usage to make sure I'm not burning through money too
outrageously.
  
 Once you're approved, you will have access to a HUIT web page titled
`<LastName>_FAS` for your Claude billing account. This page shows you
your API key, unique to you. This is what you need to provide to
Claude to enable access.
  
**TREAT THE API KEY LIKE A PASSWORD. NEVER EXPOSE IT TO ANYONE. NEVER
EXPOSE IT IN A GIT-MANAGED FILE.**
  
  
## 3. Configure your environment.  

There are a couple of ways to do this. I prefer to do it with a
Claude-specific configuration file in my home directory: Claude reads 
`.claude/settings.json` on startup. Put the following in this file
to start:

```
{
  "env": {
    "ANTHROPIC_BEDROCK_BASE_URL": "https://go.apis.huit.harvard.edu/ais-bedrock-llm/v2",
    "CLAUDE_CODE_USE_BEDROCK": "1",
    "CLAUDE_CODE_SKIP_BEDROCK_AUTH": "1",
    "ANTHROPIC_API_KEY": "<your_key_here>",
    "CLAUDE_CODE_ATTRIBUTION_HEADER": "0"
  },
}
```
  
Obviously replace `<your_key_here>` with your API key. 

Remember, DO NOT expose this configuration file to anyone.

The other way to do this is to set environment variables:

```
export ANTHROPIC_BEDROCK_BASE_URL=https://apis.huit.harvard.edu/ais-bedrock-llm/v2
export ANTHROPIC_API_KEY=<your_key_here>
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1
export CLAUDE_CODE_USE_BEDROCK=1
export CLAUDE_CODE_ATTRIBUTION_HEADER=0
```

I don't do it this way because I maintain my `.bashrc` under git
control, and I use the same `.bashrc` on a wide array of different
machines, not all of which are under my control. You can put these
shell commands in a secret file somewhere that you execute as a shell
script before you start Claude; I did it that way for a while but
found it more tedious than using `.claude/settings.json`.


## 4. First time with Claude Code

`cd` to the directory you want to work in.

Run it at the command line: `claude`

Put it in a sandbox, so it only accesses files under the current
directory (plus its own startup files in `.claude/`, I suppose) and
doesn't go rummaging around elsewhere: `/sandbox`. Select `auto-allow
mode`.

Select your model: `/model`. Select from the menu. I use Opus
4.8. Fable will generally refuse to work on comp bio code.
  
Off you go - ask it to work on something!


## More information

These notes are an abbreviated version of notes from a "Generative AI
for Scholarship" nanocourse that Chris Stubbs gave. His course is
online and gives more detail than I have:

[Setting up Anthropic API access](https://astrostubbs.github.io/GenAI-for-Scholarship/setting-up-claude-code.html)

[The Claude Code CLI](https://astrostubbs.github.io/GenAI-for-Scholarship/session3-power-user.html)
  
Anthropic also provides [notes on getting started](https://code.claude.com/docs/en/overview).



  







