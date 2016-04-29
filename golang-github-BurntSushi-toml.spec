#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : golang-github-BurntSushi-toml
Version  : bbd5bb678321a0d6e58f1099321dfa73391c1b6f
Release  : 3
URL      : https://github.com/BurntSushi/toml/archive/bbd5bb678321a0d6e58f1099321dfa73391c1b6f.tar.gz
Source0  : https://github.com/BurntSushi/toml/archive/bbd5bb678321a0d6e58f1099321dfa73391c1b6f.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : WTFPL
BuildRequires : go

%description
## TOML parser and encoder for Go with reflection
TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library `json` and `xml`
packages. This package also supports the `encoding.TextUnmarshaler` and
`encoding.TextMarshaler` interfaces so that you can define custom data
representations. (There is an example of this below.)

%prep
%setup -q -n toml-bbd5bb678321a0d6e58f1099321dfa73391c1b6f

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/BurntSushi/toml"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/BurntSushi/toml

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/BurntSushi/toml/_examples/example.go
/usr/lib/golang/src/github.com/BurntSushi/toml/cmd/toml-test-decoder/main.go
/usr/lib/golang/src/github.com/BurntSushi/toml/cmd/toml-test-encoder/main.go
/usr/lib/golang/src/github.com/BurntSushi/toml/cmd/tomlv/main.go
/usr/lib/golang/src/github.com/BurntSushi/toml/decode.go
/usr/lib/golang/src/github.com/BurntSushi/toml/decode_meta.go
/usr/lib/golang/src/github.com/BurntSushi/toml/decode_test.go
/usr/lib/golang/src/github.com/BurntSushi/toml/doc.go
/usr/lib/golang/src/github.com/BurntSushi/toml/encode.go
/usr/lib/golang/src/github.com/BurntSushi/toml/encode_test.go
/usr/lib/golang/src/github.com/BurntSushi/toml/encoding_types.go
/usr/lib/golang/src/github.com/BurntSushi/toml/encoding_types_1.1.go
/usr/lib/golang/src/github.com/BurntSushi/toml/lex.go
/usr/lib/golang/src/github.com/BurntSushi/toml/parse.go
/usr/lib/golang/src/github.com/BurntSushi/toml/type_check.go
/usr/lib/golang/src/github.com/BurntSushi/toml/type_fields.go
