#!/usr/bin/env sh

if ! [ -x "$(command -v pyenv)" ]; then
  yum install -y zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils git
  curl https://pyenv.run | bash
fi

grep -q pyenv $HOME/.bashrc
if [[ $? -eq 1 ]]; then
cat>>$HOME/.bashrc<<'EOF'
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOF
source $HOME/.bashrc
fi

pyenv install --skip-existing 2.7.16
pyenv install --skip-existing 3.7.3

pyenv virtualenv 2.7.16 1st
pyenv virtualenv 3.7.3 2st
