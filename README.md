# ZILA: ZJUIntl Learning Assistant

## Features

- [x] Get deadline of assignments from Blackboard
- [x] Get latest grades of assignments from Blackboard
- [x] Get latest announcements from Blackboard
- [ ] Get information from PeopleSoft. **I've not figured out how to do this yet. PRs and disscussions are welcome!**

## Usage

### main

It's a command-line tool that provides the abilities shown in [Features](#features).

Here is the usage of `main.py`:

1. Install dependencies: `pip install -r requirements.txt`
2. Run `main.py`. For the first time, it will create a `config.yaml` file in the same folder and you should fill your username and password in it. Only zjuam (统一身份认证) is supported now.
3. Follow the instructions and enjoy!

Another way is to download pre-built executables from [Actions](https://github.com/ZJUIntl-share/zjuintl-learning-assistant/actions). Then you can follow step 2 and 3 above.

### module `assistant`

`assistant` folder is a package that contains a class `Assistant`, which provides abilities shown in [Features](#features). Dependencies are listed in `requirements.txt` in the same folder.

For more details, please refer to [wiki](https://github.com/ZJUIntl-share/zjuintl-learning-assistant/wiki) (WIP).

## Development Notes

This project is simply a spider that replay the requests of the browser. Login process of zjuam is based on package capture and reverse engineering of javascript code. However, the analysis of PeopleSoft is too difficult for me. So any help is welcome! I think possible difficulty is the management of cookies.

## Credits

- [ZJUintl-gRPC](https://github.com/QSCTech/ZJUintl-gRPC)
- [zju-learning-assistant](https://github.com/PeiPei233/zju-learning-assistant)
