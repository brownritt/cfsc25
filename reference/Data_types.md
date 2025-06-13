# Data types

### Bits and bytes

At the most fundamental level, computers work on *bits*, short for *binary digits*, which can take one of two possible values. Computer here means specifically a *digital* computer, and the bit represents the position of a simple switch. Modern computers are in some sense a massive collection of On/Off switches.

The set of values is usually denoted `{0,1}`, but could equivalently be written as `{True,False}`, `{On,Off}`, `{Heads,Tails}`, or any other set with two elements.

Early computer development converged on the *byte* as the most convenient size for an "atomic" unit of memory, storage, or processing. A byte is 8 bits long, or in other words is an eight digit binary number. A byte can therefore take on $2^8=256$ possible values.

Roughly speaking, a letter of text takes one up byte. Numbers take up a size roughly determined by their magnitude. The number 178 can be stored in one byte, the number 19,312 requires two bytes (two bytes stacked together represent a binary number with 16 digits, which means there are $2^{16}=65536$ possible values).

Since we often deal with much larger sets of information, we use metric system prefixes:
- *kilo*, K = thousand, $10^3$
- *mega*, M = million, $10^6$
- *giga*, G = billlion, $10^9$
- *tera*, T = trillion, $10^{12}$
- *peta*, P = $10^{15}$
- *exa*, E = $10^{18}$

The exact number of bytes allocated in a computer is typically a power of two, so the above prefixes are an approximation. For example, a kilobyte, `1 KB`, is often 1024 bytes ($=2^{10}$) instead of 1000. There are special conventions for notating exact vs inexact prefixes, but none are universally accepted.

For a sense of scale, a laptop with sixteen gigabytes (`16 GB`) of memory can represent about $16\times 10^{9}\times 256 \approx 4\times 10^{12}$ different states, or is equivalent to a switchboard with about 4 trillion On/Off switches. The size of the internet has been estimated (for now...) to be on the order of 10,000 to 100,000 exabytes.

### Data types as useful abstraction

Everything a computer does can be thought of as operations on binary numbers, encoded in some number of bytes. To facilitate programming with more natural and intuitive forms of information, all modern programming languages define a (usually extensible) set of **data types**.

A data type is defined by two things: how the information is encoded in the underlying structure of bytes, and what operations can be done on data of that type. Usually only the operations interest programmers, but the encoding can matter, for example, when it is important to know how much memory is needed to store a certain amount of information in a given data type.

We'll describe some types as used in Python, but every other language will have similar types. In Python, the command `type()` returns the data type of whatever it is given as an argument (technical side note, it actually returns the "object type").

### Integer

The most simple data type is the `int` or integer, e.g. 0, 1, 2, and so on. An integer type will have well defined addition and multiplication operations, but not division, since there is no guarantee that division will produce another integer (e.g. `10/3` is not an integer). There *may* be a "modular division" operation though, which means to throw away the remainder (e.g. `10//3=3`).

Even here there are subtleties. First, one can specify the *size*, the largest integer value one needs, by the number of encoded bits. A single `int8` can represent 256 values, a single `int16` can represent 65,536 values, and so on.

Also, we've actually been describing *unsigned integers*, which take values from zero up to the largest possible integer for the size. To be precise, these are preceded by a u, as in `uint8`, `uint16`, and so on. The type `int8` is usually a *signed integer* that can take on both positive and negative values; since there are only 256 possibilities, one splits the range in half to get numbers from -127 up to +128 (ignoring some details at the end points).

### Float

The other major numerical type is *floating point*, or `float`, where point here means the decimal point, and floating refers to the ability to represent different numbers of digits after the point. Essentially all floats are defined to be signed (positive and negative values), and all of the usual operations on real numbers will be defined.

A common way to display floats is in scientific notation, e.g. `3.8174E-4`, where the `E` indicates an "exponent" or power of 10. In this example, the number is $3.8174\times 10^{-4}$.

There is again a choice of *size*, which has less to do with the magnitude of the numbers, and instead indicates the number of stored decimal places (not counting the exponent). The most common standard today is the `double`, or double precision float, which can store about 15 digits after the decimal point, and takes 8 bytes to store (also written `float64` for the number of bits).

### Equality of floats

A very common error when working with floats is to check if they are *exactly* equal, using `a==b`. Almost all floating point computations incur *round-off error*, meaning that even if the ideal mathematical operations would produce an equality, in the finite precision of the computer the numbers come out a little different. It is usually better to use something like Numpy's `isclose` function, and/or to define explicitly how much calculational error should be disregarded.

### Boolean

The Boolean type (named after George Boole) can take only `True` or `False` values. Comparisons of numbers return Boolean types, e.g. `3.1>3.0` returns the `bool` value `True`. 

Booleans ca be combined through *logical operators* such as `and` (or its bitwise version `&`) and `or` (bitwise `|`). So for example, `(3>2) & (1>2)` returns `False`, while `(3>2) | (1>2)` returns `True`. Note the parentheses; due to something called "operator precedence", it is wise to enclose each comparison in its own parentheses.

### Coercion and conversion

Most modern languages have some ability to coerce types when it seems appropriate. For example, in Python if you divide the `int` `10` by the `int` `3` (using `/`), what gets returned is a `float` that is approximately equal to 3.3333333. Also, if you add the `int` `3` to the `float` `.1415` you get the `float` `3.1415`.

Python has a trick to type an integer that you would like encoded as a float: add a decimal place. So typing `2` produces an `int`, and typing `2.0` produces a `float`.

You can try to force a conversion using operators that have the same name as the types. For example, `float(2)` produces the floating point number `2.0`. The other way doesn't use rounding, but instead truncates the decimals, so e.g. `int(2.71828)` produces the integer `2`.

Any operation that makes sense only for integers, such as specifying an index into an array, may throw an error if you use a float, even if the value of that float is a whole number. Operations often check for a correct data type, not the value. One then needs to convert with `int()` for the operation to work. For example, `range(1,2)` is valid, `range(1,2.0)` throws an error, and `range(1,int(2.0))` is again valid.

Another very common conversion is from Boolean to integer under addition; each `True` is replaced by 1, and each `False` by 0. This provides a convenient way to count the number of `True` values in an array. For example, `True+False` returns `1`, and `np.sum([True,False,True])` produces `2`. A little less obvious is that `True*4` returns `4` and `False*4` returns `0`, but this conversion is sometimes useful in making a "mask" (all values in an array matching a `True` are kept as is, and all values matching a `False` are set to zero).

### String

String data types, e.g. `str`, store text or text-like information. One sometimes sees a character type `char`, which can mean just a single character of text, or is often equivalent to strings (the name itself comes from storing "strings of characters" like a "string of pearls"). Each language has its own convention.

In Python, a string type is indicated by enclosing text in either single (`'`) or double (`"`) quotes (it makes no difference, except that the same choice must be made at beginning and end). There is also a special "multiline string" that can be enclosed in triple quotes. Other languages will use one or both types of quote symbols.

Be aware that `print` usually drops the quotes when displaying string.

Operations on strings do different things than with numbers. In Python, "adding" strings concatenates them, so `'abc'+'de'`  returns the single string `'abcde'`. Multiplying a string by an integer makes copies of the string, so `'2'*3` returns `'222'`. Note that `2` and `'2'` are totally different things to a computer. Multiplying a string by a float, or by another string, produces an error.

Strings can contain "special" or "command" characters. For example `'Quick\tJump'` represents the word `Quick`, followed by a jump to the next "tab stop", followed by the word `Jump`. The string `'Up\nDown'` represents the word `Up`, followed by the word `Down` printed below it on the next line.

Python has the concept of a *raw string*, which places an `r` before the opening quote, and means to ignore all special characters. For example, `r'a\nb'` represents four characters all on the same line (the exact set of characters `a`, `\`, `n`, and `b`). Raw strings are important for strings containing paths, which tend to have slashes in them, or when wanting to copy textual information preserving all the new lines and such.

Python also has a *format string*, that provides a convenient way to substitute computed values at the time the string is interpreted. For example if a variable `C` has the value `7.4`, the string
`f'C is equal to {C}'` 
becomes equivalent to the string 
`'C is equal to 7.4'`

### ASCII and Unicode text

Within the class of string types, there is still the question of the exact way to encode text by binary numbers. Standard encodings are needed to be able to share text across different types of machines and programming environments.

The 52 English letters (including both upper and lower case), 10 decimal digits (`0` to `9`), and two dozen or so punctuation marks (`!@.;:`, etc) can be easily encoded into a single byte. The landmark *ASCII* character encoding, still widely used today, provides a standard way of performing this encoding that can be shared across computer manufacturers, and uses the leftover space for "non-printable" and "control" characters.

For example, the English word `Cat` is represented by the sequence of numbers `67,97,116`, taking three bytes total. A device receiving the number `13` should produce a "Carriage Return", which is a non-printable character sometimes symbolized as `CR`; the name comes from ancient teletype machines, and means to return the "print head" to the start of the line. A related control character is "Line Feed", or `LF`, which tells the device to "scroll the paper" down one line. The ASCII number `7` tells a device to sound a bell (it used to be a physical bell, but is now just some beeping sound).

There is some ambiguity in how different devices interpret ASCII command characters. The most famous of these is a choice of whether a new line of text should be indicated by the combination of `CR-LF` (ASCII character `13` followed by character `10`) or simply by `CR` or simply by `LF`. The major operating systems, Windows, MacOS, and Linux, made different choices early on, and so when transferring text files between operating systems, one sometimes sees "extra" characters at the end of each line (a common case is a Windows generated text file showing a special `^M` symbol for a "redundant" `CR` character when read on a Linux machine).

Because each character is represented by exactly one byte, ASCII is limited in the number of symbols it can encode, and enforces a bias towards English speakers inherited from the early dominance of the US on computer science. A more recent standard that attempts to address these deficiencies is Unicode. Unicode can encode characters from many languages, and special symbols beyond printed text. The standard is naturally more complicated (e.g. there can be a variable number of bytes per character, and special "switches" are needed to indicate which character set is being used), and implementation across computer systems is a bit uneven, so ASCII is still used in many "raw" text situations. However, Unicode is now widespread, and is attempting to become the universal default (the Unicode subset `utf8` is a very close analogue of ASCII).

It is still risky to use Unicode characters with most "generalist" systems. For example, errors may occur when trying to use Unicode characters in file names, internet URLs, `git` repo names, and so on.

### Advanced data types

The above types are nearly universal, or at least highly similar, across languages. One thing that distinguishes different languages, and drives people's coding preferences, are what other more complex data types are available. 

For example, Python has a `list` data type, that holds a list of elements, each of which can be an arbitrary data type. For example, `[1,'hi',4.3]` is a list whose elements, in order, have types `int`, `str`, and `float`. Like strings, adding lists performs concatenation: `[1,2]+[-1]` returns `[1,2,-1]`. Multiplying by an `int` replicates: `[3,4]*2` returns `[3,4,3,4]`.

Numpy defines a new data type called an `ndarray`, or just array for short. Arrays look similar to lists, but behave very differently. For example, `np.array([3,4])*2` returns `np.array([6,8])`. Addition of arrays of the same size adds corresponding elements, while adding arrays of different sizes produces an error (except in the special case of something called "broadcasting").

There are *many* other data types. The Pandas `DataFrame` is a popular type for working with tabular data. Most languages have some concept of a `structure` or `record` (in Python the closest thing is a `dict` or dictionary), that stores "key-value" pairs that allow one to reference information by user defined names for the type of information. In fact, users can define their own data types as needed. 

The key takeaway is to be aware that types guide what operations are possible for an element of data, and how they will behave, and that sometimes one needs to specify or convert types.
