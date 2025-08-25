# Unit 0: Getting Started with Diffusion

## Overview
Welcome to the Diffusion Models Course! This unit introduces you to the fascinating world of diffusion models and gives you hands-on experience with DreamBooth, a powerful technique for personalizing image generation models.

## What You'll Learn
- What are diffusion models and how they revolutionized AI art
- Introduction to DreamBooth for model personalization
- Hands-on experience training your first diffusion model
- Understanding different applications and use cases

## DreamBooth: Personalizing Diffusion Models
DreamBooth is a technique that allows you to **personalize a Stable Diffusion model by fine-tuning it on just a handful of your own images.** Using this powerful method from [this research paper](https://arxiv.org/abs/2208.12242), you can teach a model to generate a specific subject (like your pet or a unique object) in any context you can imagine.

## Example Applications
Explore these different themes and applications:

* **Animal 🐨:** Use this theme to generate images of your pet or favourite animal hanging out in the Acropolis, swimming, or flying in space.
* **Science 🔬:** Use this theme to generate cool synthetic images of galaxies, proteins, or any domain of the natural and medical sciences.
* **Food 🍔:** Use this theme to tune Stable Diffusion on your favourite dish or cuisine.
* **Landscape 🏔:** Use this theme to generate beautiful landscapes of your favourite mountain, lake, or garden.
* **Wildcard 🔥:** Use this theme to go wild and create Stable Diffusion models for any category of your choosing!

We'll be **giving out prizes to the top 3 most liked models per theme**, and you're encouraged to submit as many models as you want! 

## Getting started

Follow the steps below to take part in this event:

1. Join the [Hugging Face Discord server](https://huggingface.co/join/discord) and check out the `#dreambooth-hackathon` channel to stay up to date with the event.
2. Launch and run the [DreamBooth notebook](https://github.com/huggingface/diffusion-models-class/blob/main/hackathon/dreambooth.ipynb) to train your models by clicking on one of the links below. Make sure you select the GPU runtime in each platform to ensure your models train fast!

| Notebook                                     | Colab                                                                                                                                                                                               | Kaggle                                                                                                                                                                                                   | Gradient                                                                                                                                                                               | Studio Lab                                                                                                                                                                                                   |
|:--------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DreamBooth Training                              | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/huggingface/diffusion-models-class/blob/main/hackathon/dreambooth.ipynb)              | [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/huggingface/diffusion-models-class/blob/main/hackathon/dreambooth.ipynb)              | [![Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/huggingface/diffusion-models-class/blob/main/hackathon/dreambooth.ipynb)              | [![Open In SageMaker Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/huggingface/diffusion-models-class/blob/main/hackathon/dreambooth.ipynb)              |

**Note 👋:** The DreamBooth notebook uses the [`CompVis/stable-diffusion-v1-4`](https://huggingface.co/CompVis/stable-diffusion-v1-4) checkpoint as the Stable Diffusion model to fine-tune. However, you are totally free to use any Stable Diffusion checkpoint that you want - you'll just have to adjust the code to load the appropriate components and the safety checker (if it exists). Some interesting models to fine-tune include:

* [`runwayml/stable-diffusion-v1-5`](https://huggingface.co/runwayml/stable-diffusion-v1-5)
* [`prompthero/openjourney`](https://huggingface.co/prompthero/openjourney)
* [`stabilityai/stable-diffusion-2`](https://huggingface.co/stabilityai/stable-diffusion-2)
* [`hakurei/waifu-diffusion`](https://huggingface.co/hakurei/waifu-diffusion)
* [`stabilityai/stable-diffusion-2-1`](https://huggingface.co/stabilityai/stable-diffusion-2-1)
* [`nitrosocke/elden-ring-diffusion`](https://huggingface.co/nitrosocke/elden-ring-diffusion)

## Evaluation & Leaderboard

To be in the running for the prizes, push one or more DreamBooth models to the Hub with the `dreambooth-hackathon` tag in the model card ([example](https://huggingface.co/lewtun/ccorgi-dog/blob/main/README.md#L9)). This is created automatically by the [DreamBooth notebook](https://github.com/huggingface/diffusion-models-class/blob/main/hackathon/dreambooth.ipynb), but you'll need to add it if you're running your own scripts.

Models are evaluated according to the number of likes they have and you can track your model's ranking on the hackathon's leaderboard:

* [DreamBooth Leaderboard](https://huggingface.co/spaces/dreambooth-hackathon/leaderboard)

## Timeline

* **December 21, 2022** - Start date
* **December 31, 2022** - Colab Pro registration deadline
* **January 22, 2023** - Final submissions deadline (closing of the leaderboard)
* **January 23-27, 2023** - Announce winners of each theme

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted.

## Prizes

We will be awarding 3 prizes per theme, where **winners are determined by the models with the most likes** on the leaderboard:

**1st place winner**

* [Hugging Face Pro subscription](https://huggingface.co/pricing) for 1 year or a $100 voucher for the [Hugging Face merch store](https://store.huggingface.co/)

**2nd place winner**

* A copy of the [_NLP with Transformers_](https://transformersbook.com/) book or a $50 voucher for the [Hugging Face merch store](https://store.huggingface.co/)

**3rd place winner**

* [Hugging Face Pro subscription](https://huggingface.co/pricing) for 1 month or a $15 voucher for the [Hugging Face merch store](https://store.huggingface.co/)

We will also provide a **certificate of completion** to all the participants that submit at least 1 DreamBooth model to the hackathon 🔥.


## Compute

Google Colab will be sponsoring this event by providing fee Colab Pro credits to 100 participants (selected randomly). We'll be giving out the credits in January 2023, and you have until December 31 to register. To register for these credits, please fill out [this form](https://docs.google.com/forms/d/e/1FAIpQLSeE_js5bxq_a_nFTglbZbQqjd6KNDD9r4YRg42kDFGSb5aoYQ/viewform).

![](https://lh3.googleusercontent.com/-l6dUgmPOKMM/X7w3nNn3OpI/AAAAAAAALAg/74fTRiPqikMURTD_Dn4PzAVADey2_6lLwCNcBGAsYHQ/s400/colab-logo-128x128.png)

## FAQ

### What data is allowed for fine-tuning?

You can use any images that belong to you or for which a permissive license allows for. If you'd like to submit a model trained on faces (e.g. as a Wildcard submission), we recommend using your own likeness. Ideally, use your own data where you can - we'd love to see your pets or favorite local landscape features, and we suspect the likes and prizes will tend to go to those who do something nice and personal 😁.

### Are other fine-tuning techniques like Textual Inversion allowed?

Absolutely! Although this hackathon is focused on DreamBooth, you're welcome (and encouraged) to experiment with other fine-tuning techniques. This also means you can use whatever frameworks, code, or services that help you make delightful models for the community to enjoy 🥰.

