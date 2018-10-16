FROM codait/max-base

ARG model_bucket=http://max-assets.s3-api.us-geo.objectstorage.softlayer.net/tf/im2txt
ARG model_file=im2txt_ckpt.tar.gz

RUN wget -nv --show-progress --progress=bar:force:noscroll ${model_bucket}/${model_file} --output-document=/workspace/assets/${model_file}
RUN tar -x -C assets/ -f assets/${model_file} -v && rm assets/${model_file}

COPY requirements.txt /workspace
RUN pip install -r requirements.txt

COPY . /workspace
RUN md5sum -c md5sums.txt # check file integrity

EXPOSE 5000

CMD python app.py
