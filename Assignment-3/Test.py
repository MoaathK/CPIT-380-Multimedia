import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from jes4py import *

# Load an image using matplotlib
image_url = 'C:\Users\m_h37\Desktop\Github\CPIT-380-Multimedia\salad.jpg'  # Replace with your image URL or local path
image = mpimg.imread(image_url)

def histoCalc(image):
    src = makePicture(image)
    print("test")
    histR = [0] * 255
    histG = [0] * 255
    histB = [0] * 255
    for x in range(src.getWidth()):
        for y in range(src.getHeight()):
            img = getPixel(src,x,y)
            rColor = getRed(img)
            gColor = getGreen(img)
            bColor = getBlue(img)
            histR[rColor] +=1
            histG[gColor] +=1
            histB[bColor] +=1


def compute_histogram(image):
    """Compute histogram for each channel."""
    histogram = [np.histogram(image[:, :, i], bins=np.arange(257))[0] for i in range(3)]
    return histogram

def equalize_histogram(image, histogram):
    """Equalize the histogram of an image."""
    output_image = np.zeros_like(image)
    for channel in range(3):
        # Calculate the histogram's CDF (Cumulative Distribution Function)
        cdf = histogram[channel].cumsum()
        # Normalize the CDF
        cdf_normalized = (cdf - cdf.min()) * 255 / (cdf.max() - cdf.min())
        cdf_normalized = cdf_normalized.astype('uint8')
        
        # If image was initially in [0, 1] range, scale it back to [0, 255]
        if image.max() <= 1.0:
            channel_data = (image[:, :, channel] * 255).astype('uint8')
        else:
            channel_data = image[:, :, channel].astype('uint8')

        # Use the normalized CDF as a mapping to transform the pixel values
        output_image[:, :, channel] = cdf_normalized[channel_data]
    return output_image


def plot_histograms(histogram):
    """Plot histograms for RGB channels."""
    colors = ['r', 'g', 'b']
    for i, color in enumerate(colors):
        plt.plot(histogram[i], color=color)
    plt.title('Histograms of RGB Channels')
    plt.show()

# Compute histograms
histograms = compute_histogram(image)

# Plot histograms
plot_histograms(histograms)

# Apply histogram equalization
equalized_image = equalize_histogram(image / 255.0, histograms)  # Ensure image is in [0, 1] range

# Display before and after images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Equalized Image')
plt.imshow(equalized_image)
plt.axis('off')

plt.show()
