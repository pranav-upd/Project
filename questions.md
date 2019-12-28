# Questions

## What's `stdint.h`?

The <stdint.h> header shall declare sets of integer types having specified widths, and shall define corresponding sets of macros. It shall also define macros that specify limits of integer types corresponding to types defined in other standard headers. 

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

It`s to represent various fixed integer data types

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE is an unsigned 8 bit integer, DWORD is unsigned 32 bit integer, LONG is signed 32 bit integer,WORD is an unsigned 16 bit integer.

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

It would be the bftype of the bmp file.

## What's the difference between `bfSize` and `biSize`?

bfsize is the bitmap file size and bisize is the bitmap image size

## What does it mean if `biHeight` is negative?

 If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in `copy.c`?

it fails to find the file

## Why is the third argument to `fread` always `1` in our code?

It`s always 1 because we need to read 1 byte from the file at a time.

## What value does `copy.c` assign to `padding` if `bi.biWidth` is `3`?

3

## What does `fseek` do?

fseek() is used to move file pointer associated with a given file to a specific position

## What is `SEEK_CUR`?

the value of SEEK_CUR is 1 no matter what's going on in the code. It's just used as a flag for fseek
