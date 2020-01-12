#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int r=0,g=0,b=0,avg=0;
    for (int i=0;i<height;i++){
        for (int j=0;j<width;j++){
            b = image[i][j].rgbtBlue;
            g = image[i][j].rgbtGreen;
            r = image[i][j].rgbtRed;
            avg = (r+b+g)/3;
            image[i][j].rgbtBlue = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtRed = avg;

        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float sepiaRed=0,sepiaGreen=0,sepiaBlue=0;
    int originalRed=0,originalGreen=0,originalBlue=0;
    for (int i=0;i<height;i++){
        for (int j=0;j<width;j++){
            originalBlue = image[i][j].rgbtBlue;
            originalGreen = image[i][j].rgbtGreen;
            originalRed = image[i][j].rgbtRed;
            sepiaRed = (0.393 * originalRed) + (0.769 * originalGreen) + (0.189 * originalBlue);
            sepiaGreen = (0.349 * originalRed) + (0.686 * originalGreen) + (0.168 * originalBlue);
            sepiaBlue = (0.272 * originalRed) + (0.534 * originalGreen) + (0.131 * originalBlue);
            originalRed = sepiaRed;
            originalGreen = sepiaGreen;
            originalBlue = sepiaBlue;
            image[i][j].rgbtRed = originalRed;
            image[i][j].rgbtGreen = originalGreen;
            image[i][j].rgbtBlue = originalBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
