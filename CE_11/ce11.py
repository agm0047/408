{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "726312bc-3a14-4c97-b575-0de3e5d1164d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7462aaec-3f94-4065-891c-bd32b4ee04b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def normalize_longitude(lon: float) ->float:\n",
    "    \"\"\" Normalize a longitude value to be in a range of (-180, 180).\"\"\"\n",
    "    if lon > 180:\n",
    "        return lon - 360\n",
    "    elif lon < -180:\n",
    "        return lon + 360\n",
    "    else:\n",
    "        return lon  "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
