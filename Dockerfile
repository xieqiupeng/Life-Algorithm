# Life-Algorithm image
# 1. 通过挂载镜像直接操作仓库
# 1. 打包成新的镜像
# 1. 推送镜像到服务器和镜像仓库

FROM ubuntu:16.04
RUN mkdir /"技术和专长"
WORKDIR /"技术和专长"
ADD ./ /var/app/libTandE
EXPOSE 8084

#CMD ["java","-jar","libs/app-0.0.1-SNAPSHOT-shadow.jar"]
#CMD ["java","-cp","libs/YueTing-0.0.1-SNAPSHOT.jar", "com.keyi.yueting.YuetingApplication"]
#FROM java:openjdk-8-alpine
#VOLUME /tmp
#ADD YueTing-0.0.1-SNAPSHOT.jar app.jar
#RUN sh -c 'touch /app.jar'
##ENV JAVA_OPTS=""
#ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app.jar" ]
