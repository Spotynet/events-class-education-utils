FROM public.ecr.aws/lambda/python:3.9

# WORKDIR /create_pdf

RUN yum -y install wget
# RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.amazonlinux2.x86_64.rpm
# RUN yum -y install ./wkhtmltox-0.12.6-1.amazonlinux2.x86_64.rpm

COPY requirements.txt  .
RUN  python3.9 -m pip install --upgrade pip && python3.9 -m pip install -r requirements.txt --no-cache -t .

COPY ./ ./ 

CMD [ "app.lambda_handler" ] 
