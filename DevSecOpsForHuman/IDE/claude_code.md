

# install

## on ubuntu

curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo bash -
sudo apt-get install -y nodejs
node --version

npm install -g @anthropic-ai/claude-code
claude --version

# uninstall

npm uninstall -g @anthropic-ai/claude-code

root用户无法bypass permission，加一条设定即可:
IS_SANDBOX=1 claude --dangerously-skip-permissions 
