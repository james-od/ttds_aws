'use strict';

//Pop this in a folder with S3GETtest.htm
//Open S3GETtest.htm in a browser, everything -should- just work
//without needing to install anything else, if not just let me know
//Open the console and check to see if there was any output.

// (Please don't save the secretAccessKey into versionControl)
var s3 = new AWS.S3(
  { accessKeyId: '',
    secretAccessKey: ''
  }
);

s3.getObject(
  { Bucket: "test-bucket-ttdsgroup", Key: "testfile.txt" },
  function (error, data) {
    if (error != null) {
      alert("Failed to retrieve object: " + error);
    } else {
      var decoded = new TextDecoder("utf-8").decode(data.Body);
      console.log(decoded)
    }
  }
);
