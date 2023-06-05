# Server Event Stream model
A very simple python app that applies the server event stream model

# How to run?
* Install python in your machine
* Install Python libraries using `pip install -r requirements.txt`
* Run the program by using `python server-event-modal.py`
* Open the following link `http://127.0.0.1:8888/sse` or use the following code in the browser console:

```js
const sse = new SourceEvent();
sse.onmessage = console.log
```