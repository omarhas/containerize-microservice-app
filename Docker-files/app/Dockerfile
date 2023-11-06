FROM tomcat:8-jre11
LABEL "Project"="Vprofile"
LABEL "Author"="Imran"

RUN rm -rf /usr/local/tomcat/webapps/*
COPY target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8081
CMD ["catalina.sh", "run"]
WORKDIR /usr/local/tomcat/
VOLUME /usr/local/tomcat/webapps
