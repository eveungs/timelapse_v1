{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/eveungs/timelapse_v1/blob/main/TIMELAPSE_APP_v1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0WKGQfgVNr9_"
      },
      "source": [
        "<a href=\"https://githubtocolab.com/gee-community/geemap/blob/master/examples/notebooks/27_timelapse_app.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open in Colab\"/></a>\n",
        "\n",
        "Uncomment the following line to install [geemap](https://geemap.org) if needed."
      ],
      "id": "0WKGQfgVNr9_"
    },
    {
      "cell_type": "markdown",
      "source": [
        "**PASO 1.** Correr esta línea."
      ],
      "metadata": {
        "id": "hFJGtQszPVF4"
      },
      "id": "hFJGtQszPVF4"
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "ooP3WgsGNr-M",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "4b878766-236e-4854-f3d9-8d746b97bfaf"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: geemap in /usr/local/lib/python3.10/dist-packages (0.22.1)\n",
            "Requirement already satisfied: bqplot in /usr/local/lib/python3.10/dist-packages (from geemap) (0.12.39)\n",
            "Requirement already satisfied: colour in /usr/local/lib/python3.10/dist-packages (from geemap) (0.1.5)\n",
            "Requirement already satisfied: earthengine-api>=0.1.347 in /usr/local/lib/python3.10/dist-packages (from geemap) (0.1.350)\n",
            "Requirement already satisfied: eerepr>=0.0.4 in /usr/local/lib/python3.10/dist-packages (from geemap) (0.0.4)\n",
            "Requirement already satisfied: folium>=0.13.0 in /usr/local/lib/python3.10/dist-packages (from geemap) (0.14.0)\n",
            "Requirement already satisfied: geocoder in /usr/local/lib/python3.10/dist-packages (from geemap) (1.38.1)\n",
            "Requirement already satisfied: ipyevents in /usr/local/lib/python3.10/dist-packages (from geemap) (2.0.1)\n",
            "Requirement already satisfied: ipyfilechooser>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from geemap) (0.6.0)\n",
            "Requirement already satisfied: ipyleaflet>=0.17.0 in /usr/local/lib/python3.10/dist-packages (from geemap) (0.17.2)\n",
            "Requirement already satisfied: ipytree in /usr/local/lib/python3.10/dist-packages (from geemap) (0.2.2)\n",
            "Requirement already satisfied: matplotlib in /usr/local/lib/python3.10/dist-packages (from geemap) (3.7.1)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from geemap) (1.22.4)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from geemap) (1.5.3)\n",
            "Requirement already satisfied: plotly in /usr/local/lib/python3.10/dist-packages (from geemap) (5.13.1)\n",
            "Requirement already satisfied: pyperclip in /usr/local/lib/python3.10/dist-packages (from geemap) (1.8.2)\n",
            "Requirement already satisfied: pyshp>=2.1.3 in /usr/local/lib/python3.10/dist-packages (from geemap) (2.3.1)\n",
            "Requirement already satisfied: python-box in /usr/local/lib/python3.10/dist-packages (from geemap) (7.0.1)\n",
            "Requirement already satisfied: scooby in /usr/local/lib/python3.10/dist-packages (from geemap) (0.7.2)\n",
            "Requirement already satisfied: google-cloud-storage in /usr/local/lib/python3.10/dist-packages (from earthengine-api>=0.1.347->geemap) (2.8.0)\n",
            "Requirement already satisfied: google-api-python-client>=1.12.1 in /usr/local/lib/python3.10/dist-packages (from earthengine-api>=0.1.347->geemap) (2.84.0)\n",
            "Requirement already satisfied: google-auth>=1.4.1 in /usr/local/lib/python3.10/dist-packages (from earthengine-api>=0.1.347->geemap) (2.17.3)\n",
            "Requirement already satisfied: google-auth-httplib2>=0.0.3 in /usr/local/lib/python3.10/dist-packages (from earthengine-api>=0.1.347->geemap) (0.1.0)\n",
            "Requirement already satisfied: httplib2<1dev,>=0.9.2 in /usr/local/lib/python3.10/dist-packages (from earthengine-api>=0.1.347->geemap) (0.21.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from earthengine-api>=0.1.347->geemap) (2.27.1)\n",
            "Requirement already satisfied: branca>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from folium>=0.13.0->geemap) (0.6.0)\n",
            "Requirement already satisfied: jinja2>=2.9 in /usr/local/lib/python3.10/dist-packages (from folium>=0.13.0->geemap) (3.1.2)\n",
            "Requirement already satisfied: ipywidgets in /usr/local/lib/python3.10/dist-packages (from ipyfilechooser>=0.6.0->geemap) (7.7.1)\n",
            "Requirement already satisfied: traittypes<3,>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from ipyleaflet>=0.17.0->geemap) (0.2.1)\n",
            "Requirement already satisfied: xyzservices>=2021.8.1 in /usr/local/lib/python3.10/dist-packages (from ipyleaflet>=0.17.0->geemap) (2023.5.0)\n",
            "Requirement already satisfied: traitlets>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from bqplot->geemap) (5.7.1)\n",
            "Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas->geemap) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->geemap) (2022.7.1)\n",
            "Requirement already satisfied: click in /usr/local/lib/python3.10/dist-packages (from geocoder->geemap) (8.1.3)\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.10/dist-packages (from geocoder->geemap) (0.18.3)\n",
            "Requirement already satisfied: ratelim in /usr/local/lib/python3.10/dist-packages (from geocoder->geemap) (0.1.6)\n",
            "Requirement already satisfied: six in /usr/local/lib/python3.10/dist-packages (from geocoder->geemap) (1.16.0)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->geemap) (1.0.7)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib->geemap) (0.11.0)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->geemap) (4.39.3)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->geemap) (1.4.4)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->geemap) (23.1)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib->geemap) (8.4.0)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib->geemap) (3.0.9)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from plotly->geemap) (8.2.2)\n",
            "Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5 in /usr/local/lib/python3.10/dist-packages (from google-api-python-client>=1.12.1->earthengine-api>=0.1.347->geemap) (2.11.0)\n",
            "Requirement already satisfied: uritemplate<5,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from google-api-python-client>=1.12.1->earthengine-api>=0.1.347->geemap) (4.1.1)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.4.1->earthengine-api>=0.1.347->geemap) (5.3.0)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.4.1->earthengine-api>=0.1.347->geemap) (0.3.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.4.1->earthengine-api>=0.1.347->geemap) (4.9)\n",
            "Requirement already satisfied: ipykernel>=4.5.1 in /usr/local/lib/python3.10/dist-packages (from ipywidgets->ipyfilechooser>=0.6.0->geemap) (5.5.6)\n",
            "Requirement already satisfied: ipython-genutils~=0.2.0 in /usr/local/lib/python3.10/dist-packages (from ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.2.0)\n",
            "Requirement already satisfied: widgetsnbextension~=3.6.0 in /usr/local/lib/python3.10/dist-packages (from ipywidgets->ipyfilechooser>=0.6.0->geemap) (3.6.4)\n",
            "Requirement already satisfied: ipython>=4.0.0 in /usr/local/lib/python3.10/dist-packages (from ipywidgets->ipyfilechooser>=0.6.0->geemap) (7.34.0)\n",
            "Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from ipywidgets->ipyfilechooser>=0.6.0->geemap) (3.0.7)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2>=2.9->folium>=0.13.0->geemap) (2.1.2)\n",
            "Requirement already satisfied: google-cloud-core<3.0dev,>=2.3.0 in /usr/local/lib/python3.10/dist-packages (from google-cloud-storage->earthengine-api>=0.1.347->geemap) (2.3.2)\n",
            "Requirement already satisfied: google-resumable-media>=2.3.2 in /usr/local/lib/python3.10/dist-packages (from google-cloud-storage->earthengine-api>=0.1.347->geemap) (2.5.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->earthengine-api>=0.1.347->geemap) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->earthengine-api>=0.1.347->geemap) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests->earthengine-api>=0.1.347->geemap) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->earthengine-api>=0.1.347->geemap) (3.4)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.10/dist-packages (from ratelim->geocoder->geemap) (4.4.2)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0dev,>=1.56.2 in /usr/local/lib/python3.10/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client>=1.12.1->earthengine-api>=0.1.347->geemap) (1.59.0)\n",
            "Requirement already satisfied: protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5 in /usr/local/lib/python3.10/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client>=1.12.1->earthengine-api>=0.1.347->geemap) (3.20.3)\n",
            "Requirement already satisfied: google-crc32c<2.0dev,>=1.0 in /usr/local/lib/python3.10/dist-packages (from google-resumable-media>=2.3.2->google-cloud-storage->earthengine-api>=0.1.347->geemap) (1.5.0)\n",
            "Requirement already satisfied: jupyter-client in /usr/local/lib/python3.10/dist-packages (from ipykernel>=4.5.1->ipywidgets->ipyfilechooser>=0.6.0->geemap) (6.1.12)\n",
            "Requirement already satisfied: tornado>=4.2 in /usr/local/lib/python3.10/dist-packages (from ipykernel>=4.5.1->ipywidgets->ipyfilechooser>=0.6.0->geemap) (6.3.1)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.10/dist-packages (from ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (67.7.2)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.10/dist-packages (from ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.18.2)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.10/dist-packages (from ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.7.5)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (3.0.38)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.10/dist-packages (from ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (2.14.0)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.10/dist-packages (from ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.2.0)\n",
            "Requirement already satisfied: matplotlib-inline in /usr/local/lib/python3.10/dist-packages (from ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.1.6)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.10/dist-packages (from ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (4.8.0)\n",
            "Requirement already satisfied: pyasn1<0.6.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth>=1.4.1->earthengine-api>=0.1.347->geemap) (0.5.0)\n",
            "Requirement already satisfied: notebook>=4.4.1 in /usr/local/lib/python3.10/dist-packages (from widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (6.4.8)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/lib/python3.10/dist-packages (from jedi>=0.16->ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.8.3)\n",
            "Requirement already satisfied: pyzmq>=17 in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (23.2.1)\n",
            "Requirement already satisfied: argon2-cffi in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (21.3.0)\n",
            "Requirement already satisfied: jupyter-core>=4.6.1 in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (5.3.0)\n",
            "Requirement already satisfied: nbformat in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (5.8.0)\n",
            "Requirement already satisfied: nbconvert in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (6.5.4)\n",
            "Requirement already satisfied: nest-asyncio>=1.5 in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (1.5.6)\n",
            "Requirement already satisfied: Send2Trash>=1.8.0 in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (1.8.0)\n",
            "Requirement already satisfied: terminado>=0.8.3 in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.17.1)\n",
            "Requirement already satisfied: prometheus-client in /usr/local/lib/python3.10/dist-packages (from notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.16.0)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.10/dist-packages (from pexpect>4.3->ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.10/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=4.0.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.2.6)\n",
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.10/dist-packages (from jupyter-core>=4.6.1->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (3.3.0)\n",
            "Requirement already satisfied: argon2-cffi-bindings in /usr/local/lib/python3.10/dist-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (21.2.0)\n",
            "Requirement already satisfied: lxml in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (4.9.2)\n",
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (4.11.2)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (6.0.0)\n",
            "Requirement already satisfied: defusedxml in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.7.1)\n",
            "Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.4)\n",
            "Requirement already satisfied: jupyterlab-pygments in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.2.2)\n",
            "Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.8.4)\n",
            "Requirement already satisfied: nbclient>=0.5.0 in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.7.4)\n",
            "Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (1.5.0)\n",
            "Requirement already satisfied: tinycss2 in /usr/local/lib/python3.10/dist-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (1.2.1)\n",
            "Requirement already satisfied: fastjsonschema in /usr/local/lib/python3.10/dist-packages (from nbformat->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (2.16.3)\n",
            "Requirement already satisfied: jsonschema>=2.6 in /usr/local/lib/python3.10/dist-packages (from nbformat->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (4.3.3)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=2.6->nbformat->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (23.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=2.6->nbformat->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.19.3)\n",
            "Requirement already satisfied: cffi>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (1.15.1)\n",
            "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (2.4.1)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.10/dist-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (0.5.1)\n",
            "Requirement already satisfied: pycparser in /usr/local/lib/python3.10/dist-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.6.0->ipywidgets->ipyfilechooser>=0.6.0->geemap) (2.21)\n"
          ]
        }
      ],
      "source": [
        "!pip install geemap"
      ],
      "id": "ooP3WgsGNr-M"
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Paso 2.** Importar librerías."
      ],
      "metadata": {
        "id": "46_GM7abPSpI"
      },
      "id": "46_GM7abPSpI"
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "XiAUNlGfNr-Q"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "import ee\n",
        "import geemap\n",
        "import ipywidgets as widgets"
      ],
      "id": "XiAUNlGfNr-Q"
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Paso 3.** Carga de mapa base.\n",
        "\n",
        "Este paso pedirá un código de verificación, que se obtiene a través de ingresar a la URL generada al correr la siguiente línea de codigo."
      ],
      "metadata": {
        "id": "6KaXuUi3Xqse"
      },
      "id": "6KaXuUi3Xqse"
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "eMYbx1yJNr-S",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 621,
          "referenced_widgets": [
            "10748fd3c5184927bacbb1ef01a8a446",
            "50b74ec577de4665992d932a051f7b96",
            "e09950dc2e59464cb0d7fa6f47f58516",
            "a61a35b1e09f43a980a3197c32812a0c",
            "cce358ece1c0415a8966092185134981",
            "456814c74a314660a46560af3e294f98",
            "6cec6922eb0f4e46bfb021f5486fbf6a",
            "ed6ee682b7174e76bc7bb3943f9a0d39",
            "7fbc427099fe4936873687e35d470dd2",
            "f432223cdbd24e5ba8143baf19295565",
            "304f55a045154e178b5224f38e8108d3",
            "dcd85a7976ea4c529fee86ab2ab8fdd6",
            "73daaca51459425eae6ea81dc9f79f3c",
            "8278edd691ea42bf96d78e660902271a",
            "b89d414d91e5402180cec0996f92c59f",
            "0c1fdff6a212432ba291d545591b1c5b",
            "9149e3ffe0ce4f4bbfb0f9ff37c58ca5",
            "aad4566cf1f14731a174ccca7667ab0f",
            "31dc91bd4ed14cf6aaf66da85e0c1fb4",
            "598ca6f5f6384d818289100ff08178c1",
            "a9a7f368dca2451ea56351be3ed60c74",
            "95e02a3dc2fb4b2a9555472cffeca697",
            "c4b14a8f63ce4f38b2a2e4fbeba2abd0",
            "e4f10138f91c4ad1abdcda6c425518ec",
            "9eff75ca52174bdaaa8baefbe5129746",
            "630b037229b6407194d1599263589d7d",
            "7faeca1ff6fa48b792760c18e2e80812",
            "fdc9f01a30b34e3a9d8456d12a69a4c4",
            "acda2b725d2940e995eb8f2b0c08fbd2"
          ]
        },
        "outputId": "8b6bd114-7083-42d1-e260-68d7cf299587"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Map(center=[-40, -64], controls=(WidgetControl(options=['position', 'transparent_bg'], widget=HBox(children=(T…"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "10748fd3c5184927bacbb1ef01a8a446"
            }
          },
          "metadata": {
            "application/vnd.jupyter.widget-view+json": {
              "colab": {
                "custom_widget_manager": {
                  "url": "https://ssl.gstatic.com/colaboratory-static/widgets/colab-cdn-widget-manager/b3e629b1971e1542/manager.min.js"
                }
              }
            }
          }
        }
      ],
      "source": [
        "Map = geemap.Map(center=(-40, -64), zoom=4)\n",
        "Map.add_basemap('HYBRID')\n",
        "Map"
      ],
      "id": "eMYbx1yJNr-S"
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Paso 4.** Trazar en el mapa, con las herramientas de dibujo, un poligono.\n",
        "Se deberá dibujar sólo un polígono, de lo contrario el resultado se aplicará sobre el último dibujado."
      ],
      "metadata": {
        "id": "XV2kEWg5YB3k"
      },
      "id": "XV2kEWg5YB3k"
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Paso 5.**"
      ],
      "metadata": {
        "id": "GCw5jQ87aM_W"
      },
      "id": "GCw5jQ87aM_W"
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "VUq4MKApNr-T"
      },
      "outputs": [],
      "source": [
        "#out_dir = os.path.join(os.path.expanduser('~'), 'Downloads')\n",
        "#if not os.path.exists(out_dir):\n",
        "#    os.makedirs(out_dir)"
      ],
      "id": "VUq4MKApNr-T"
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "I3VtLk8iNr-U"
      },
      "outputs": [],
      "source": [
        "style = {'description_width': 'initial'}\n",
        "title = widgets.Text(\n",
        "    description='Title:', value='Landsat Timelapse', width=200, style=style\n",
        ")"
      ],
      "id": "I3VtLk8iNr-U"
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "h39jiwTdNr-W"
      },
      "outputs": [],
      "source": [
        "bands = widgets.Dropdown(\n",
        "    description='Select RGB Combo:',\n",
        "    options=[\n",
        "        'Red/Green/Blue',\n",
        "        'NIR/Red/Green',\n",
        "        'SWIR2/SWIR1/NIR',\n",
        "        'NIR/SWIR1/Red',\n",
        "        'SWIR2/NIR/Red',\n",
        "        'SWIR2/SWIR1/Red',\n",
        "        'SWIR1/NIR/Blue',\n",
        "        'NIR/SWIR1/Blue',\n",
        "        'SWIR2/NIR/Green',\n",
        "        'SWIR1/NIR/Red',\n",
        "    ],\n",
        "    value='NIR/Red/Green',\n",
        "    style=style,\n",
        ")"
      ],
      "id": "h39jiwTdNr-W"
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Paso 6.** Ajustar parametros segun las necesidades."
      ],
      "metadata": {
        "id": "YqDe_bztaS-P"
      },
      "id": "YqDe_bztaS-P"
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "3Lt-b55NNr-a",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 49,
          "referenced_widgets": [
            "aca251a58432431db436d5db5e8f907f",
            "584cf1dd07914ff0a7a6dd2ea4c3fad1",
            "238054750e32427283aca43718ac8f38",
            "2d8fc7d21c994c98875ce4e00ff2809d",
            "bc3d83c441a74cd7bfb3ccff645502dc",
            "ada5411896604709aed5b8c58ff5720f",
            "23ec69d7dc3e441780b6105177756830",
            "3094a4ab5e54473c8c9e0106fa5c3194"
          ]
        },
        "outputId": "98bb4b39-4966-4ae5-ad19-6b35bd19fc1f"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "HBox(children=(Text(value='Landsat Timelapse', description='Title:', style=DescriptionStyle(description_width=…"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "aca251a58432431db436d5db5e8f907f"
            }
          },
          "metadata": {
            "application/vnd.jupyter.widget-view+json": {
              "colab": {
                "custom_widget_manager": {
                  "url": "https://ssl.gstatic.com/colaboratory-static/widgets/colab-cdn-widget-manager/b3e629b1971e1542/manager.min.js"
                }
              }
            }
          }
        }
      ],
      "source": [
        "hbox1 = widgets.HBox([title, bands])\n",
        "hbox1"
      ],
      "id": "3Lt-b55NNr-a"
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "aPC6XyyPNr-b"
      },
      "outputs": [],
      "source": [
        "start_year = widgets.IntSlider(\n",
        "    description='Start Year:', value=1984, min=1984, max=2021, style=style\n",
        ")"
      ],
      "id": "aPC6XyyPNr-b"
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "g-i28jP7Nr-d"
      },
      "outputs": [],
      "source": [
        "end_year = widgets.IntSlider(\n",
        "    description='End Year:', value=2021, min=1984, max=2021, style=style\n",
        ")"
      ],
      "id": "g-i28jP7Nr-d"
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "GbPUp9fpNr-e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 49,
          "referenced_widgets": [
            "6de18895e7f9492d97edce507cc95841",
            "6adaccb0ce6542498a28c952cb7fc830",
            "88dfd86d0233444086147df0a066041d",
            "0339c83fdd2245a29682eeff2b8c9c5b",
            "a0e7ed8b067d4a4cb10e16404333e547",
            "0869d43868a14e7aa90401f6b8202f96",
            "6c32b2a9e81f4002bcc18073afc73e66",
            "94263c6a6c5544449f1406230d2ea863"
          ]
        },
        "outputId": "f1b728ac-8d2c-4caa-e7b0-202d39b013b5"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "HBox(children=(IntSlider(value=1984, description='Start Year:', max=2021, min=1984, style=SliderStyle(descript…"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "6de18895e7f9492d97edce507cc95841"
            }
          },
          "metadata": {
            "application/vnd.jupyter.widget-view+json": {
              "colab": {
                "custom_widget_manager": {
                  "url": "https://ssl.gstatic.com/colaboratory-static/widgets/colab-cdn-widget-manager/b3e629b1971e1542/manager.min.js"
                }
              }
            }
          }
        }
      ],
      "source": [
        "hbox2 = widgets.HBox([start_year, end_year])\n",
        "hbox2"
      ],
      "id": "GbPUp9fpNr-e"
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "LdB3CijSNr-f"
      },
      "outputs": [],
      "source": [
        "speed = widgets.IntSlider(\n",
        "    description='Frames per second:',\n",
        "    tooltip='Frames per second:',\n",
        "    value=10,\n",
        "    min=1,\n",
        "    max=30,\n",
        "    style=style,\n",
        ")"
      ],
      "id": "LdB3CijSNr-f"
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "asT8htSaNr-g"
      },
      "outputs": [],
      "source": [
        "download = widgets.Checkbox(value=False, description='Download the GIF', style=style)"
      ],
      "id": "asT8htSaNr-g"
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "1D3wTQHNNr-h",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 49,
          "referenced_widgets": [
            "df32361933284329944863e5fdb92b5a",
            "add327f5c6cb4529b96630d2953a7149",
            "81ff993173794cd7866530a71f69c9cf",
            "7cfc257a8f724be2b1265427b1337bba",
            "54d469bfb6d4428f9af6062459568a4a",
            "99861ebfbbed42b5a428344d2ad62549",
            "6fbbbbfe411944059f02ddc3058ec2b0",
            "e325a1c146584e78bfcb5cd2954908df"
          ]
        },
        "outputId": "de05cc16-95ce-4db6-8de2-5c511c6c9487"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "HBox(children=(IntSlider(value=10, description='Frames per second:', max=30, min=1, style=SliderStyle(descript…"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "df32361933284329944863e5fdb92b5a"
            }
          },
          "metadata": {
            "application/vnd.jupyter.widget-view+json": {
              "colab": {
                "custom_widget_manager": {
                  "url": "https://ssl.gstatic.com/colaboratory-static/widgets/colab-cdn-widget-manager/b3e629b1971e1542/manager.min.js"
                }
              }
            }
          }
        }
      ],
      "source": [
        "hbox3 = widgets.HBox([speed, download])\n",
        "hbox3"
      ],
      "id": "1D3wTQHNNr-h"
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "1hS6vJMvNr-i"
      },
      "outputs": [],
      "source": [
        "font_size = widgets.IntSlider(\n",
        "    description='Font size:', value=30, min=10, max=50, style=style\n",
        ")"
      ],
      "id": "1hS6vJMvNr-i"
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "JIuy261QNr-j"
      },
      "outputs": [],
      "source": [
        "font_color = widgets.ColorPicker(\n",
        "    concise=False, description='Font color:', value='white', style=style\n",
        ")"
      ],
      "id": "JIuy261QNr-j"
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "id": "M7n-g9lONr-k"
      },
      "outputs": [],
      "source": [
        "progress_bar_color = widgets.ColorPicker(\n",
        "    concise=False, description='Progress bar color:', value='blue', style=style\n",
        ")"
      ],
      "id": "M7n-g9lONr-k"
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "hZuUrY2JNr-l",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 49,
          "referenced_widgets": [
            "5db07e5c532e414f8df47867e25eff18",
            "2cee93af148c471eb0bb471f1a6063c8",
            "2f7d097a6ee64c92889d6610aa5599e8",
            "b9e6f2845a154043b75c9958218c46e4",
            "1270984378bc4a9ca48891b5069654c7",
            "8763ab0aee1849ae99e85d5ac5f946ff",
            "7b7427b581bd4bcdac25bf72f643d499",
            "8af0e22b1cf94e3c9148eb346efa43be",
            "fcd873fd86444ab7b9d6aa766ed6602d",
            "066d28ffb9264f84b46eb839acc7db9d",
            "84c7572ab44d4dc984c456557172295f"
          ]
        },
        "outputId": "cd46c7dd-9549-49fc-f78a-b807e0448a7b"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "HBox(children=(IntSlider(value=30, description='Font size:', max=50, min=10, style=SliderStyle(description_wid…"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "5db07e5c532e414f8df47867e25eff18"
            }
          },
          "metadata": {
            "application/vnd.jupyter.widget-view+json": {
              "colab": {
                "custom_widget_manager": {
                  "url": "https://ssl.gstatic.com/colaboratory-static/widgets/colab-cdn-widget-manager/b3e629b1971e1542/manager.min.js"
                }
              }
            }
          }
        }
      ],
      "source": [
        "hbox4 = widgets.HBox([font_size, font_color, progress_bar_color])\n",
        "hbox4"
      ],
      "id": "hZuUrY2JNr-l"
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "_AIbWDeXNr-m"
      },
      "outputs": [],
      "source": [
        "submit = widgets.Button(\n",
        "    description='Submit',\n",
        "    button_style='primary',\n",
        "    tooltip='Click the submit the request to create timelapse',\n",
        "    style=style,\n",
        ")\n",
        "\n",
        "output = widgets.Output()"
      ],
      "id": "_AIbWDeXNr-m"
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "Qcm1JozFNr-m"
      },
      "outputs": [],
      "source": [
        "def submit_clicked(b):\n",
        "    with output:\n",
        "        output.clear_output()\n",
        "        if start_year.value >= end_year.value:\n",
        "            print('The end year must be great than the start year.')\n",
        "            return\n",
        "        print('Computing...')\n",
        "\n",
        "        Map.add_landsat_ts_gif(\n",
        "            roi=Map.user_roi,\n",
        "            label=title.value,\n",
        "            start_year=start_year.value,\n",
        "            end_year=end_year.value,\n",
        "            start_date='05-01',\n",
        "            end_date='10-31',\n",
        "            bands=bands.value.split('/'),\n",
        "            font_color=font_color.value,\n",
        "            frames_per_second=speed.value,\n",
        "            font_size=font_size.value,\n",
        "            progress_bar_color=progress_bar_color.value,\n",
        "            download=download.value,\n",
        "        )\n",
        "\n",
        "\n",
        "submit.on_click(submit_clicked)"
      ],
      "id": "Qcm1JozFNr-m"
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "id": "yvvKvB8eNr-n",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 49,
          "referenced_widgets": [
            "ff83ed5eed52416996b1d4e42cc5bcb4",
            "ff31b284d08943de928e6b04833313dd",
            "01f563102a7d497cbd6ae9a7f9d1ba15"
          ]
        },
        "outputId": "b1d4b101-fa52-4361-c513-d23ac1455e58"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Button(button_style='primary', description='Submit', style=ButtonStyle(), tooltip='Click the submit the reques…"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "ff83ed5eed52416996b1d4e42cc5bcb4"
            }
          },
          "metadata": {
            "application/vnd.jupyter.widget-view+json": {
              "colab": {
                "custom_widget_manager": {
                  "url": "https://ssl.gstatic.com/colaboratory-static/widgets/colab-cdn-widget-manager/b3e629b1971e1542/manager.min.js"
                }
              }
            }
          }
        }
      ],
      "source": [
        "submit"
      ],
      "id": "yvvKvB8eNr-n"
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "PjD1fL1VNr-n",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 658,
          "referenced_widgets": [
            "f5a21f2378ab47709ff1646270f8df9b",
            "8e5bf13ed6b44fd9849b55848103bfa0"
          ]
        },
        "outputId": "d99e9fdd-ade7-4694-cf3b-8572a3b41b9f"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "Output()"
            ],
            "application/vnd.jupyter.widget-view+json": {
              "version_major": 2,
              "version_minor": 0,
              "model_id": "f5a21f2378ab47709ff1646270f8df9b"
            }
          },
          "metadata": {
            "application/vnd.jupyter.widget-view+json": {
              "colab": {
                "custom_widget_manager": {
                  "url": "https://ssl.gstatic.com/colaboratory-static/widgets/colab-cdn-widget-manager/b3e629b1971e1542/manager.min.js"
                }
              }
            }
          }
        }
      ],
      "source": [
        "output"
      ],
      "id": "PjD1fL1VNr-n"
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "widgets": {
      "application/vnd.jupyter.widget-state+json": {
        "10748fd3c5184927bacbb1ef01a8a446": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletMapModel",
          "model_module_version": "^0.17",
          "state": {
            "_dom_classes": [],
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletMapModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletMapView",
            "bottom": 640815,
            "bounce_at_zoom_limits": true,
            "box_zoom": true,
            "center": [
              -37.0209205486642,
              -62.59220123291016
            ],
            "close_popup_on_click": true,
            "controls": [
              "IPY_MODEL_50b74ec577de4665992d932a051f7b96",
              "IPY_MODEL_e09950dc2e59464cb0d7fa6f47f58516",
              "IPY_MODEL_a61a35b1e09f43a980a3197c32812a0c",
              "IPY_MODEL_cce358ece1c0415a8966092185134981",
              "IPY_MODEL_456814c74a314660a46560af3e294f98",
              "IPY_MODEL_6cec6922eb0f4e46bfb021f5486fbf6a",
              "IPY_MODEL_ed6ee682b7174e76bc7bb3943f9a0d39",
              "IPY_MODEL_7fbc427099fe4936873687e35d470dd2"
            ],
            "crs": {
              "name": "EPSG3857",
              "custom": false
            },
            "default_style": "IPY_MODEL_f432223cdbd24e5ba8143baf19295565",
            "double_click_zoom": true,
            "dragging": true,
            "dragging_style": "IPY_MODEL_304f55a045154e178b5224f38e8108d3",
            "east": -62.28424072265626,
            "fullscreen": false,
            "inertia": true,
            "inertia_deceleration": 3000,
            "inertia_max_speed": 1500,
            "interpolation": "bilinear",
            "keyboard": true,
            "keyboard_pan_offset": 80,
            "keyboard_zoom_offset": 1,
            "layers": [
              "IPY_MODEL_dcd85a7976ea4c529fee86ab2ab8fdd6",
              "IPY_MODEL_73daaca51459425eae6ea81dc9f79f3c",
              "IPY_MODEL_8278edd691ea42bf96d78e660902271a",
              "IPY_MODEL_acda2b725d2940e995eb8f2b0c08fbd2"
            ],
            "layout": "IPY_MODEL_b89d414d91e5402180cec0996f92c59f",
            "left": 341078,
            "max_zoom": 24,
            "min_zoom": null,
            "modisdate": "2023-05-31",
            "north": -36.93864177246069,
            "options": [
              "bounce_at_zoom_limits",
              "box_zoom",
              "center",
              "close_popup_on_click",
              "double_click_zoom",
              "dragging",
              "fullscreen",
              "inertia",
              "inertia_deceleration",
              "inertia_max_speed",
              "interpolation",
              "keyboard",
              "keyboard_pan_offset",
              "keyboard_zoom_offset",
              "max_zoom",
              "min_zoom",
              "prefer_canvas",
              "scroll_wheel_zoom",
              "tap",
              "tap_tolerance",
              "touch_zoom",
              "world_copy_jump",
              "zoom",
              "zoom_animation_threshold",
              "zoom_delta",
              "zoom_snap"
            ],
            "panes": {},
            "prefer_canvas": false,
            "right": 342872,
            "scroll_wheel_zoom": true,
            "south": -37.10311031724964,
            "style": "IPY_MODEL_f432223cdbd24e5ba8143baf19295565",
            "tap": true,
            "tap_tolerance": 15,
            "top": 640215,
            "touch_zoom": true,
            "west": -62.90016174316407,
            "window_url": "https://c4tvc7rdb5v-496ff2e9c6d22116-0-colab.googleusercontent.com/outputframe.html?vrz=colab-20230530-060140-RC00_536351130",
            "world_copy_jump": false,
            "zoom": 12,
            "zoom_animation_threshold": 4,
            "zoom_delta": 1,
            "zoom_snap": 1
          }
        },
        "50b74ec577de4665992d932a051f7b96": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletWidgetControlModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletWidgetControlModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletWidgetControlView",
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "options": [
              "position",
              "transparent_bg"
            ],
            "position": "topleft",
            "transparent_bg": false,
            "widget": "IPY_MODEL_9149e3ffe0ce4f4bbfb0f9ff37c58ca5"
          }
        },
        "e09950dc2e59464cb0d7fa6f47f58516": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletZoomControlModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletZoomControlModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletZoomControlView",
            "options": [
              "position",
              "zoom_in_text",
              "zoom_in_title",
              "zoom_out_text",
              "zoom_out_title"
            ],
            "position": "topleft",
            "zoom_in_text": "+",
            "zoom_in_title": "Zoom in",
            "zoom_out_text": "-",
            "zoom_out_title": "Zoom out"
          }
        },
        "a61a35b1e09f43a980a3197c32812a0c": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletScaleControlModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletScaleControlModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletScaleControlView",
            "imperial": true,
            "max_width": 100,
            "metric": true,
            "options": [
              "imperial",
              "max_width",
              "metric",
              "position",
              "update_when_idle"
            ],
            "position": "bottomleft",
            "update_when_idle": false
          }
        },
        "cce358ece1c0415a8966092185134981": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletFullScreenControlModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletFullScreenControlModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletFullScreenControlView",
            "options": [
              "position"
            ],
            "position": "topleft"
          }
        },
        "456814c74a314660a46560af3e294f98": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletMeasureControlModel",
          "model_module_version": "^0.17",
          "state": {
            "_custom_units": {},
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletMeasureControlModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletMeasureControlView",
            "active_color": "orange",
            "capture_z_index": 10000,
            "completed_color": "#C8F2BE",
            "options": [
              "active_color",
              "capture_z_index",
              "completed_color",
              "popup_options",
              "position",
              "primary_area_unit",
              "primary_length_unit",
              "secondary_area_unit",
              "secondary_length_unit"
            ],
            "popup_options": {
              "className": "leaflet-measure-resultpopup",
              "autoPanPadding": [
                10,
                10
              ]
            },
            "position": "bottomleft",
            "primary_area_unit": "acres",
            "primary_length_unit": "kilometers",
            "secondary_area_unit": null,
            "secondary_length_unit": null
          }
        },
        "6cec6922eb0f4e46bfb021f5486fbf6a": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletAttributionControlModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletAttributionControlModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletAttributionControlView",
            "options": [
              "position",
              "prefix"
            ],
            "position": "bottomright",
            "prefix": "ipyleaflet"
          }
        },
        "ed6ee682b7174e76bc7bb3943f9a0d39": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletDrawControlModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletDrawControlModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletDrawControlView",
            "circle": {
              "shapeOptions": {
                "color": "#3388ff"
              }
            },
            "circlemarker": {},
            "data": [
              {
                "type": "Feature",
                "properties": {
                  "style": {
                    "stroke": true,
                    "color": "#3388ff",
                    "weight": 4,
                    "opacity": 0.5,
                    "fill": true,
                    "fillColor": null,
                    "fillOpacity": 0.2,
                    "clickable": true
                  }
                },
                "geometry": {
                  "type": "Polygon",
                  "coordinates": [
                    [
                      [
                        -62.75116,
                        -37.059561
                      ],
                      [
                        -62.700691,
                        -36.980341
                      ],
                      [
                        -62.575722,
                        -36.975404
                      ],
                      [
                        -62.562675,
                        -37.079011
                      ],
                      [
                        -62.674599,
                        -37.082571
                      ],
                      [
                        -62.75116,
                        -37.059561
                      ]
                    ]
                  ]
                }
              }
            ],
            "edit": true,
            "marker": {
              "shapeOptions": {
                "color": "#3388ff"
              }
            },
            "options": [
              "position"
            ],
            "polygon": {
              "shapeOptions": {}
            },
            "polyline": {
              "shapeOptions": {}
            },
            "position": "topleft",
            "rectangle": {
              "shapeOptions": {
                "color": "#3388ff"
              }
            },
            "remove": true
          }
        },
        "7fbc427099fe4936873687e35d470dd2": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletWidgetControlModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletWidgetControlModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletWidgetControlView",
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "options": [
              "position",
              "transparent_bg"
            ],
            "position": "topright",
            "transparent_bg": false,
            "widget": "IPY_MODEL_aad4566cf1f14731a174ccca7667ab0f"
          }
        },
        "f432223cdbd24e5ba8143baf19295565": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletMapStyleModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletMapStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "cursor": "grab"
          }
        },
        "304f55a045154e178b5224f38e8108d3": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletMapStyleModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletMapStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "cursor": "move"
          }
        },
        "dcd85a7976ea4c529fee86ab2ab8fdd6": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletTileLayerModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletTileLayerModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletTileLayerView",
            "attribution": "&copy; <a href=\"https://www.openstreetmap.org/copyright\">OpenStreetMap</a> contributors",
            "base": true,
            "bottom": true,
            "bounds": null,
            "detect_retina": false,
            "loading": false,
            "max_native_zoom": null,
            "max_zoom": 19,
            "min_native_zoom": null,
            "min_zoom": 1,
            "name": "OpenStreetMap.Mapnik",
            "no_wrap": false,
            "opacity": 1,
            "options": [
              "attribution",
              "bounds",
              "detect_retina",
              "max_native_zoom",
              "max_zoom",
              "min_native_zoom",
              "min_zoom",
              "no_wrap",
              "tile_size",
              "tms",
              "zoom_offset"
            ],
            "pane": "",
            "popup": null,
            "popup_max_height": null,
            "popup_max_width": 300,
            "popup_min_width": 50,
            "show_loading": false,
            "subitems": [],
            "tile_size": 256,
            "tms": false,
            "url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            "visible": true,
            "zoom_offset": 0
          }
        },
        "73daaca51459425eae6ea81dc9f79f3c": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletTileLayerModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletTileLayerModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletTileLayerView",
            "attribution": "Google",
            "base": false,
            "bottom": true,
            "bounds": null,
            "detect_retina": false,
            "loading": false,
            "max_native_zoom": null,
            "max_zoom": 24,
            "min_native_zoom": null,
            "min_zoom": 0,
            "name": "Google Maps",
            "no_wrap": false,
            "opacity": 1,
            "options": [
              "attribution",
              "bounds",
              "detect_retina",
              "max_native_zoom",
              "max_zoom",
              "min_native_zoom",
              "min_zoom",
              "no_wrap",
              "tile_size",
              "tms",
              "zoom_offset"
            ],
            "pane": "",
            "popup": null,
            "popup_max_height": null,
            "popup_max_width": 300,
            "popup_min_width": 50,
            "show_loading": false,
            "subitems": [],
            "tile_size": 256,
            "tms": false,
            "url": "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
            "visible": true,
            "zoom_offset": 0
          }
        },
        "8278edd691ea42bf96d78e660902271a": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletTileLayerModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletTileLayerModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletTileLayerView",
            "attribution": "Google",
            "base": false,
            "bottom": true,
            "bounds": null,
            "detect_retina": false,
            "loading": false,
            "max_native_zoom": null,
            "max_zoom": 24,
            "min_native_zoom": null,
            "min_zoom": 0,
            "name": "Google Hybrid",
            "no_wrap": false,
            "opacity": 1,
            "options": [
              "attribution",
              "bounds",
              "detect_retina",
              "max_native_zoom",
              "max_zoom",
              "min_native_zoom",
              "min_zoom",
              "no_wrap",
              "tile_size",
              "tms",
              "zoom_offset"
            ],
            "pane": "",
            "popup": null,
            "popup_max_height": null,
            "popup_max_width": 300,
            "popup_min_width": 50,
            "show_loading": false,
            "subitems": [],
            "tile_size": 256,
            "tms": false,
            "url": "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
            "visible": true,
            "zoom_offset": 0
          }
        },
        "b89d414d91e5402180cec0996f92c59f": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": "600px",
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "0c1fdff6a212432ba291d545591b1c5b": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletMapStyleModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletMapStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "cursor": "grab"
          }
        },
        "9149e3ffe0ce4f4bbfb0f9ff37c58ca5": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_31dc91bd4ed14cf6aaf66da85e0c1fb4"
            ],
            "layout": "IPY_MODEL_598ca6f5f6384d818289100ff08178c1"
          }
        },
        "aad4566cf1f14731a174ccca7667ab0f": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "VBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "VBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "VBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_a9a7f368dca2451ea56351be3ed60c74"
            ],
            "layout": "IPY_MODEL_95e02a3dc2fb4b2a9555472cffeca697"
          }
        },
        "31dc91bd4ed14cf6aaf66da85e0c1fb4": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ToggleButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ToggleButtonModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ToggleButtonView",
            "button_style": "",
            "description": "",
            "description_tooltip": null,
            "disabled": false,
            "icon": "globe",
            "layout": "IPY_MODEL_c4b14a8f63ce4f38b2a2e4fbeba2abd0",
            "style": "IPY_MODEL_e4f10138f91c4ad1abdcda6c425518ec",
            "tooltip": "Search location/data",
            "value": false
          }
        },
        "598ca6f5f6384d818289100ff08178c1": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "a9a7f368dca2451ea56351be3ed60c74": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ToggleButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ToggleButtonModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ToggleButtonView",
            "button_style": "",
            "description": "",
            "description_tooltip": null,
            "disabled": false,
            "icon": "wrench",
            "layout": "IPY_MODEL_9eff75ca52174bdaaa8baefbe5129746",
            "style": "IPY_MODEL_630b037229b6407194d1599263589d7d",
            "tooltip": "Toolbar",
            "value": false
          }
        },
        "95e02a3dc2fb4b2a9555472cffeca697": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "c4b14a8f63ce4f38b2a2e4fbeba2abd0": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": "28px",
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": "0px 0px 0px 4px",
            "right": null,
            "top": null,
            "visibility": null,
            "width": "28px"
          }
        },
        "e4f10138f91c4ad1abdcda6c425518ec": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "9eff75ca52174bdaaa8baefbe5129746": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": "28px",
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": "0px 0px 0px 4px",
            "right": null,
            "top": null,
            "visibility": null,
            "width": "28px"
          }
        },
        "630b037229b6407194d1599263589d7d": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": ""
          }
        },
        "7faeca1ff6fa48b792760c18e2e80812": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletTileLayerModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletTileLayerModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletTileLayerView",
            "attribution": "Google Earth Engine",
            "base": false,
            "bottom": true,
            "bounds": null,
            "detect_retina": false,
            "loading": true,
            "max_native_zoom": null,
            "max_zoom": 18,
            "min_native_zoom": null,
            "min_zoom": 0,
            "name": "Drawn Features",
            "no_wrap": false,
            "opacity": 0.5,
            "options": [
              "attribution",
              "bounds",
              "detect_retina",
              "max_native_zoom",
              "max_zoom",
              "min_native_zoom",
              "min_zoom",
              "no_wrap",
              "tile_size",
              "tms",
              "zoom_offset"
            ],
            "pane": "",
            "popup": null,
            "popup_max_height": null,
            "popup_max_width": 300,
            "popup_min_width": 50,
            "show_loading": false,
            "subitems": [],
            "tile_size": 256,
            "tms": false,
            "url": "https://earthengine.googleapis.com/v1alpha/projects/earthengine-legacy/maps/48ab970aec899da15ff08adf37e5e791-e48db0f22bf20d8aff8524f38bd7f368/tiles/{z}/{x}/{y}",
            "visible": false,
            "zoom_offset": 0
          }
        },
        "fdc9f01a30b34e3a9d8456d12a69a4c4": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletTileLayerModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletTileLayerModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletTileLayerView",
            "attribution": "Google Earth Engine",
            "base": false,
            "bottom": true,
            "bounds": null,
            "detect_retina": false,
            "loading": false,
            "max_native_zoom": null,
            "max_zoom": 18,
            "min_native_zoom": null,
            "min_zoom": 0,
            "name": "Drawn Features",
            "no_wrap": false,
            "opacity": 0.5,
            "options": [
              "attribution",
              "bounds",
              "detect_retina",
              "max_native_zoom",
              "max_zoom",
              "min_native_zoom",
              "min_zoom",
              "no_wrap",
              "tile_size",
              "tms",
              "zoom_offset"
            ],
            "pane": "",
            "popup": null,
            "popup_max_height": null,
            "popup_max_width": 300,
            "popup_min_width": 50,
            "show_loading": false,
            "subitems": [],
            "tile_size": 256,
            "tms": false,
            "url": "https://earthengine.googleapis.com/v1alpha/projects/earthengine-legacy/maps/509aa8b26e789ea6cd5301d2020cc21a-1c90fad5663b8423c87f974f8318efaa/tiles/{z}/{x}/{y}",
            "visible": false,
            "zoom_offset": 0
          }
        },
        "acda2b725d2940e995eb8f2b0c08fbd2": {
          "model_module": "jupyter-leaflet",
          "model_name": "LeafletTileLayerModel",
          "model_module_version": "^0.17",
          "state": {
            "_model_module": "jupyter-leaflet",
            "_model_module_version": "^0.17",
            "_model_name": "LeafletTileLayerModel",
            "_view_count": null,
            "_view_module": "jupyter-leaflet",
            "_view_module_version": "^0.17",
            "_view_name": "LeafletTileLayerView",
            "attribution": "Google Earth Engine",
            "base": false,
            "bottom": true,
            "bounds": null,
            "detect_retina": false,
            "loading": false,
            "max_native_zoom": null,
            "max_zoom": 18,
            "min_native_zoom": null,
            "min_zoom": 0,
            "name": "Drawn Features",
            "no_wrap": false,
            "opacity": 0.5,
            "options": [
              "attribution",
              "bounds",
              "detect_retina",
              "max_native_zoom",
              "max_zoom",
              "min_native_zoom",
              "min_zoom",
              "no_wrap",
              "tile_size",
              "tms",
              "zoom_offset"
            ],
            "pane": "",
            "popup": null,
            "popup_max_height": null,
            "popup_max_width": 300,
            "popup_min_width": 50,
            "show_loading": false,
            "subitems": [],
            "tile_size": 256,
            "tms": false,
            "url": "https://earthengine.googleapis.com/v1alpha/projects/earthengine-legacy/maps/d89a93e61f14a18a0bda442849693c7b-fd7b75f46508e2025665f35e55f5d9ce/tiles/{z}/{x}/{y}",
            "visible": false,
            "zoom_offset": 0
          }
        },
        "aca251a58432431db436d5db5e8f907f": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_584cf1dd07914ff0a7a6dd2ea4c3fad1",
              "IPY_MODEL_238054750e32427283aca43718ac8f38"
            ],
            "layout": "IPY_MODEL_2d8fc7d21c994c98875ce4e00ff2809d"
          }
        },
        "584cf1dd07914ff0a7a6dd2ea4c3fad1": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "TextModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "TextModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "TextView",
            "continuous_update": true,
            "description": "Title:",
            "description_tooltip": null,
            "disabled": false,
            "layout": "IPY_MODEL_bc3d83c441a74cd7bfb3ccff645502dc",
            "placeholder": "​",
            "style": "IPY_MODEL_ada5411896604709aed5b8c58ff5720f",
            "value": "Landsat Timelapse"
          }
        },
        "238054750e32427283aca43718ac8f38": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DropdownModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DropdownModel",
            "_options_labels": [
              "Red/Green/Blue",
              "NIR/Red/Green",
              "SWIR2/SWIR1/NIR",
              "NIR/SWIR1/Red",
              "SWIR2/NIR/Red",
              "SWIR2/SWIR1/Red",
              "SWIR1/NIR/Blue",
              "NIR/SWIR1/Blue",
              "SWIR2/NIR/Green",
              "SWIR1/NIR/Red"
            ],
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "DropdownView",
            "description": "Select RGB Combo:",
            "description_tooltip": null,
            "disabled": false,
            "index": 4,
            "layout": "IPY_MODEL_23ec69d7dc3e441780b6105177756830",
            "style": "IPY_MODEL_3094a4ab5e54473c8c9e0106fa5c3194"
          }
        },
        "2d8fc7d21c994c98875ce4e00ff2809d": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "bc3d83c441a74cd7bfb3ccff645502dc": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "ada5411896604709aed5b8c58ff5720f": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial"
          }
        },
        "23ec69d7dc3e441780b6105177756830": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "3094a4ab5e54473c8c9e0106fa5c3194": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial"
          }
        },
        "6de18895e7f9492d97edce507cc95841": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_6adaccb0ce6542498a28c952cb7fc830",
              "IPY_MODEL_88dfd86d0233444086147df0a066041d"
            ],
            "layout": "IPY_MODEL_0339c83fdd2245a29682eeff2b8c9c5b"
          }
        },
        "6adaccb0ce6542498a28c952cb7fc830": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "IntSliderModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "IntSliderModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "IntSliderView",
            "continuous_update": true,
            "description": "Start Year:",
            "description_tooltip": null,
            "disabled": false,
            "layout": "IPY_MODEL_a0e7ed8b067d4a4cb10e16404333e547",
            "max": 2021,
            "min": 1984,
            "orientation": "horizontal",
            "readout": true,
            "readout_format": "d",
            "step": 1,
            "style": "IPY_MODEL_0869d43868a14e7aa90401f6b8202f96",
            "value": 1990
          }
        },
        "88dfd86d0233444086147df0a066041d": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "IntSliderModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "IntSliderModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "IntSliderView",
            "continuous_update": true,
            "description": "End Year:",
            "description_tooltip": null,
            "disabled": false,
            "layout": "IPY_MODEL_6c32b2a9e81f4002bcc18073afc73e66",
            "max": 2021,
            "min": 1984,
            "orientation": "horizontal",
            "readout": true,
            "readout_format": "d",
            "step": 1,
            "style": "IPY_MODEL_94263c6a6c5544449f1406230d2ea863",
            "value": 2015
          }
        },
        "0339c83fdd2245a29682eeff2b8c9c5b": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "a0e7ed8b067d4a4cb10e16404333e547": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "0869d43868a14e7aa90401f6b8202f96": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "SliderStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "SliderStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial",
            "handle_color": null
          }
        },
        "6c32b2a9e81f4002bcc18073afc73e66": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "94263c6a6c5544449f1406230d2ea863": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "SliderStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "SliderStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial",
            "handle_color": null
          }
        },
        "df32361933284329944863e5fdb92b5a": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_add327f5c6cb4529b96630d2953a7149",
              "IPY_MODEL_81ff993173794cd7866530a71f69c9cf"
            ],
            "layout": "IPY_MODEL_7cfc257a8f724be2b1265427b1337bba"
          }
        },
        "add327f5c6cb4529b96630d2953a7149": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "IntSliderModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "IntSliderModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "IntSliderView",
            "continuous_update": true,
            "description": "Frames per second:",
            "description_tooltip": null,
            "disabled": false,
            "layout": "IPY_MODEL_54d469bfb6d4428f9af6062459568a4a",
            "max": 30,
            "min": 1,
            "orientation": "horizontal",
            "readout": true,
            "readout_format": "d",
            "step": 1,
            "style": "IPY_MODEL_99861ebfbbed42b5a428344d2ad62549",
            "value": 9
          }
        },
        "81ff993173794cd7866530a71f69c9cf": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "CheckboxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "CheckboxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "CheckboxView",
            "description": "Download the GIF",
            "description_tooltip": null,
            "disabled": false,
            "indent": true,
            "layout": "IPY_MODEL_6fbbbbfe411944059f02ddc3058ec2b0",
            "style": "IPY_MODEL_e325a1c146584e78bfcb5cd2954908df",
            "value": false
          }
        },
        "7cfc257a8f724be2b1265427b1337bba": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "54d469bfb6d4428f9af6062459568a4a": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "99861ebfbbed42b5a428344d2ad62549": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "SliderStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "SliderStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial",
            "handle_color": null
          }
        },
        "6fbbbbfe411944059f02ddc3058ec2b0": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "e325a1c146584e78bfcb5cd2954908df": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial"
          }
        },
        "5db07e5c532e414f8df47867e25eff18": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "HBoxModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "HBoxModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "HBoxView",
            "box_style": "",
            "children": [
              "IPY_MODEL_2cee93af148c471eb0bb471f1a6063c8",
              "IPY_MODEL_2f7d097a6ee64c92889d6610aa5599e8",
              "IPY_MODEL_b9e6f2845a154043b75c9958218c46e4"
            ],
            "layout": "IPY_MODEL_1270984378bc4a9ca48891b5069654c7"
          }
        },
        "2cee93af148c471eb0bb471f1a6063c8": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "IntSliderModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "IntSliderModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "IntSliderView",
            "continuous_update": true,
            "description": "Font size:",
            "description_tooltip": null,
            "disabled": false,
            "layout": "IPY_MODEL_8763ab0aee1849ae99e85d5ac5f946ff",
            "max": 50,
            "min": 10,
            "orientation": "horizontal",
            "readout": true,
            "readout_format": "d",
            "step": 1,
            "style": "IPY_MODEL_7b7427b581bd4bcdac25bf72f643d499",
            "value": 30
          }
        },
        "2f7d097a6ee64c92889d6610aa5599e8": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ColorPickerModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ColorPickerModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ColorPickerView",
            "concise": false,
            "description": "Font color:",
            "description_tooltip": null,
            "disabled": false,
            "layout": "IPY_MODEL_8af0e22b1cf94e3c9148eb346efa43be",
            "style": "IPY_MODEL_fcd873fd86444ab7b9d6aa766ed6602d",
            "value": "white"
          }
        },
        "b9e6f2845a154043b75c9958218c46e4": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ColorPickerModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ColorPickerModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ColorPickerView",
            "concise": false,
            "description": "Progress bar color:",
            "description_tooltip": null,
            "disabled": false,
            "layout": "IPY_MODEL_066d28ffb9264f84b46eb839acc7db9d",
            "style": "IPY_MODEL_84c7572ab44d4dc984c456557172295f",
            "value": "blue"
          }
        },
        "1270984378bc4a9ca48891b5069654c7": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "8763ab0aee1849ae99e85d5ac5f946ff": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "7b7427b581bd4bcdac25bf72f643d499": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "SliderStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "SliderStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial",
            "handle_color": null
          }
        },
        "8af0e22b1cf94e3c9148eb346efa43be": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "fcd873fd86444ab7b9d6aa766ed6602d": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial"
          }
        },
        "066d28ffb9264f84b46eb839acc7db9d": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "84c7572ab44d4dc984c456557172295f": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "DescriptionStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "DescriptionStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "description_width": "initial"
          }
        },
        "ff83ed5eed52416996b1d4e42cc5bcb4": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonModel",
          "model_module_version": "1.5.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ButtonModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/controls",
            "_view_module_version": "1.5.0",
            "_view_name": "ButtonView",
            "button_style": "primary",
            "description": "Submit",
            "disabled": false,
            "icon": "",
            "layout": "IPY_MODEL_ff31b284d08943de928e6b04833313dd",
            "style": "IPY_MODEL_01f563102a7d497cbd6ae9a7f9d1ba15",
            "tooltip": "Click the submit the request to create timelapse"
          }
        },
        "ff31b284d08943de928e6b04833313dd": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        },
        "01f563102a7d497cbd6ae9a7f9d1ba15": {
          "model_module": "@jupyter-widgets/controls",
          "model_name": "ButtonStyleModel",
          "model_module_version": "1.5.0",
          "state": {
            "_model_module": "@jupyter-widgets/controls",
            "_model_module_version": "1.5.0",
            "_model_name": "ButtonStyleModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "StyleView",
            "button_color": null,
            "font_weight": ""
          }
        },
        "f5a21f2378ab47709ff1646270f8df9b": {
          "model_module": "@jupyter-widgets/output",
          "model_name": "OutputModel",
          "model_module_version": "1.0.0",
          "state": {
            "_dom_classes": [],
            "_model_module": "@jupyter-widgets/output",
            "_model_module_version": "1.0.0",
            "_model_name": "OutputModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/output",
            "_view_module_version": "1.0.0",
            "_view_name": "OutputView",
            "layout": "IPY_MODEL_8e5bf13ed6b44fd9849b55848103bfa0",
            "msg_id": "",
            "outputs": [
              {
                "output_type": "stream",
                "name": "stdout",
                "text": [
                  "Computing...\n",
                  "Generating URL...\n"
                ]
              },
              {
                "output_type": "stream",
                "name": "stdout",
                "text": [
                  "Downloading GIF image from https://earthengine.googleapis.com/v1alpha/projects/earthengine-legacy/videoThumbnails/a74f4651c0fd72fc2a7267470a625c11-8da0d58f537a56ff91fb76adb2b70df5:getPixels\n",
                  "Please wait ...\n"
                ]
              },
              {
                "output_type": "stream",
                "name": "stdout",
                "text": [
                  "The GIF image has been saved to: /tmp/53d84aa7-1181-4518-ae2a-6bbdbc285da7.gif\n"
                ]
              },
              {
                "output_type": "error",
                "ename": "Exception",
                "evalue": "ignored",
                "traceback": [
                  "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
                  "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
                  "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/geemap/timelapse.py\u001b[0m in \u001b[0;36mlandsat_timelapse\u001b[0;34m(roi, out_gif, start_year, end_year, start_date, end_date, bands, vis_params, dimensions, frames_per_second, crs, apply_fmask, nd_bands, nd_threshold, nd_palette, overlay_data, overlay_color, overlay_width, overlay_opacity, frequency, date_format, title, title_xy, add_text, text_xy, text_sequence, font_type, font_size, font_color, add_progress_bar, progress_bar_color, progress_bar_height, loop, mp4, fading)\u001b[0m\n\u001b[1;32m   2813\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mos\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexists\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mout_gif\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2814\u001b[0;31m             \u001b[0mreduce_gif_size\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mout_gif\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2815\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
                  "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/geemap/timelapse.py\u001b[0m in \u001b[0;36mreduce_gif_size\u001b[0;34m(in_gif, out_gif)\u001b[0m\n\u001b[1;32m    667\u001b[0m     \"\"\"\n\u001b[0;32m--> 668\u001b[0;31m     \u001b[0;32mimport\u001b[0m \u001b[0mffmpeg\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    669\u001b[0m     \u001b[0;32mimport\u001b[0m \u001b[0mwarnings\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
                  "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'ffmpeg'",
                  "\nDuring handling of the above exception, another exception occurred:\n",
                  "\u001b[0;31mException\u001b[0m                                 Traceback (most recent call last)",
                  "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/geemap/geemap.py\u001b[0m in \u001b[0;36madd_landsat_ts_gif\u001b[0;34m(self, layer_name, roi, label, start_year, end_year, start_date, end_date, bands, vis_params, dimensions, frames_per_second, font_size, font_color, add_progress_bar, progress_bar_color, progress_bar_height, out_gif, download, apply_fmask, nd_bands, nd_threshold, nd_palette)\u001b[0m\n\u001b[1;32m   2792\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2793\u001b[0;31m             in_gif = landsat_timelapse(\n\u001b[0m\u001b[1;32m   2794\u001b[0m                 \u001b[0mroi\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mroi\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
                  "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/geemap/timelapse.py\u001b[0m in \u001b[0;36mlandsat_timelapse\u001b[0;34m(roi, out_gif, start_year, end_year, start_date, end_date, bands, vis_params, dimensions, frames_per_second, crs, apply_fmask, nd_bands, nd_threshold, nd_palette, overlay_data, overlay_color, overlay_width, overlay_opacity, frequency, date_format, title, title_xy, add_text, text_xy, text_sequence, font_type, font_size, font_color, add_progress_bar, progress_bar_color, progress_bar_height, loop, mp4, fading)\u001b[0m\n\u001b[1;32m   2827\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2828\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2829\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
                  "\u001b[0;31mException\u001b[0m: No module named 'ffmpeg'",
                  "\nDuring handling of the above exception, another exception occurred:\n",
                  "\u001b[0;31mException\u001b[0m                                 Traceback (most recent call last)",
                  "\u001b[0;32m<ipython-input-19-ee8bf125a856>\u001b[0m in \u001b[0;36msubmit_clicked\u001b[0;34m(b)\u001b[0m\n\u001b[1;32m      7\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Computing...'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m         Map.add_landsat_ts_gif(\n\u001b[0m\u001b[1;32m     10\u001b[0m             \u001b[0mroi\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mMap\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0muser_roi\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m             \u001b[0mlabel\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtitle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalue\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
                  "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/geemap/geemap.py\u001b[0m in \u001b[0;36madd_landsat_ts_gif\u001b[0;34m(self, layer_name, roi, label, start_year, end_year, start_date, end_date, bands, vis_params, dimensions, frames_per_second, font_size, font_color, add_progress_bar, progress_bar_color, progress_bar_height, out_gif, download, apply_fmask, nd_bands, nd_threshold, nd_palette)\u001b[0m\n\u001b[1;32m   2871\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2872\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2873\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0me\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2874\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2875\u001b[0m     def to_html(\n",
                  "\u001b[0;31mException\u001b[0m: No module named 'ffmpeg'"
                ]
              }
            ]
          }
        },
        "8e5bf13ed6b44fd9849b55848103bfa0": {
          "model_module": "@jupyter-widgets/base",
          "model_name": "LayoutModel",
          "model_module_version": "1.2.0",
          "state": {
            "_model_module": "@jupyter-widgets/base",
            "_model_module_version": "1.2.0",
            "_model_name": "LayoutModel",
            "_view_count": null,
            "_view_module": "@jupyter-widgets/base",
            "_view_module_version": "1.2.0",
            "_view_name": "LayoutView",
            "align_content": null,
            "align_items": null,
            "align_self": null,
            "border": null,
            "bottom": null,
            "display": null,
            "flex": null,
            "flex_flow": null,
            "grid_area": null,
            "grid_auto_columns": null,
            "grid_auto_flow": null,
            "grid_auto_rows": null,
            "grid_column": null,
            "grid_gap": null,
            "grid_row": null,
            "grid_template_areas": null,
            "grid_template_columns": null,
            "grid_template_rows": null,
            "height": null,
            "justify_content": null,
            "justify_items": null,
            "left": null,
            "margin": null,
            "max_height": null,
            "max_width": null,
            "min_height": null,
            "min_width": null,
            "object_fit": null,
            "object_position": null,
            "order": null,
            "overflow": null,
            "overflow_x": null,
            "overflow_y": null,
            "padding": null,
            "right": null,
            "top": null,
            "visibility": null,
            "width": null
          }
        }
      }
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}