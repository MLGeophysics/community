# Overview

Let's train a neural network to generate well logs! A generator can be used to interpolate missing data, or as implicit regularization for inversion.

Step 1: Find digital well logs for training. An easy way to download thousands of well logs in bulk is to get them from the [Kansas Geologic Survey](http://www.kgs.ku.edu/PRS/Scans/Log_Summary/index.html).

Step 2: Prepare the data to use for training. We've gone through and selected just over 4000 wells to use as a training set. These are all the wells that have uninterrupted RILD logs in the depth interval from 400 ft to 4000 ft, sampled every foot.

Step 3: Choose a generator algorithm. There are a few ways to do this. One is to build a variational autoencoder, or VAE (see the autoencoder project on this site for more). Another is to build a generative adversarial network (GAN). Thirdly, we could combine the two to form a VAE-GAN; see [here](https://towardsdatascience.com/what-the-heck-are-vae-gans-17b86023588a) for an explanation. Ideally, let's try all three and compare the results!

