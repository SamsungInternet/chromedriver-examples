# Samsung Internet ChromeDriver Examples

## Prerequisites

* Example scripts currently for Python v2 only.
* Requires Samsung Internet v8.2 [which is in Beta](https://medium.com/samsung-internet-dev/hello-samsung-internet-8-2-beta-521e4b215fb3) at the time of writing.
* Requires ChromeDriver v2.36. [Try the download link here](https://chromedriver.storage.googleapis.com/index.html?path=2.36/).
* Connect the Android device over USB and ensure that USB debugging is enabled.
* Check that `adb devices` lists the device.
* Ensure that ChromeDriver is in your path (and that it resolves to the v2.36 binary): `chromedriver --version`.

## Running the tests

Then:

```
python [file path for script]
```

E.g. `python 01-load-page.py`

## Support

If you run into a problem or have a question, you can [raise an issue here](https://github.com/samsunginternet/support/issues).
