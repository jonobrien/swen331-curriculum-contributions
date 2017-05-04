# swen331-votd

Heap Overflow Allowing for arbitrary code execution

This vulnerability allows a malicious actor to craft input to the binary in such a way to redirect execution.

# Reproduction Steps

1. unzip heap_overflow.zip
2. cd into the directory created
3. make build
4. make unsafe
5. make safe

* You will see warnings about pointers and errors from make regarding permissions, these are fine.
* If you run the commands directly, you will see there are no errors. The overflow happens, or it does not.

# Vulnerability fix

To fix this vulnerability the input buffer length was checked with the call to strncpy.  strncpy takes in a length parameter, therefore preventing the overflow.

[stack version](https://github.com/jonobrien/swen331-curriculum-contributions/blob/master/stack.py)
