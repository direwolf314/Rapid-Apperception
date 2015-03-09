@ECHO OFF

REM testing c (io)
python add_keyword.py c getchar io
python add_keyword.py c gets io
python add_keyword.py c scanf io

REM input/output stuff
python add_keyword.py java Java.io io
python add_keyword.py java java.util.zip io
python add_keyword.py java java.util.jar io
python add_keyword.py java FileInputStream io
python add_keyword.py java ObjectInputStream io
python add_keyword.py java FilterInputStream io
python add_keyword.py java PipedInputStream io
python add_keyword.py java SequenceInputStream io
python add_keyword.py java StringBufferInputStream io
python add_keyword.py java BufferedReader io
python add_keyword.py java ByteArrayInputStream io
python add_keyword.py java CharArrayReader io
python add_keyword.py java File io
python add_keyword.py java ObjectInputStream io
python add_keyword.py java PipedInputStream io
python add_keyword.py java StreamTokenizer io
python add_keyword.py java getResourceAsStream io
python add_keyword.py java java.io.FileReader io
python add_keyword.py java java.io.FileWriter io
python add_keyword.py java java.io.RandomAccessFile io
python add_keyword.py java java.io.File io
python add_keyword.py java java.io.FileOutputStream io
python add_keyword.py java mkdir io
python add_keyword.py java renameTo io

REM servlet stuff
python add_keyword.py java javax.servlet. servlet
python add_keyword.py java getParameterNames servlet
python add_keyword.py java getParameterValues servlet
python add_keyword.py java getParameter servlet
python add_keyword.py java getParameterMap servlet
python add_keyword.py java getScheme servlet
python add_keyword.py java getProtocol servlet
python add_keyword.py java getContentType servlet
python add_keyword.py java getServerName servlet
python add_keyword.py java getRemoteAddr servlet
python add_keyword.py java getRemoteHost servlet
python add_keyword.py java getRealPath servlet
python add_keyword.py java getLocalName servlet
python add_keyword.py java getAttribute servlet
python add_keyword.py java getAttributeNames servlet
python add_keyword.py java getLocalAddr servlet
python add_keyword.py java getAuthType servlet
python add_keyword.py java getRemoteUser servlet
python add_keyword.py java getCookies servlet
python add_keyword.py java isSecure servlet
python add_keyword.py java HttpServletRequest servlet
python add_keyword.py java getQueryString servlet
python add_keyword.py java getHeaderNames servlet
python add_keyword.py java getHeaders servlet
python add_keyword.py java getPrincipal servlet
python add_keyword.py java getUserPrincipal servlet
python add_keyword.py java isUserInRole servlet
python add_keyword.py java getInputStream servlet
python add_keyword.py java getOutputStream servlet
python add_keyword.py java getWriter servlet
python add_keyword.py java addCookie servlet
python add_keyword.py java addHeader servlet
python add_keyword.py java setHeader servlet
python add_keyword.py java setAttribute servlet
python add_keyword.py java putValue servlet
python add_keyword.py java javax.servlet.http.Cookie servlet
python add_keyword.py java getName servlet
python add_keyword.py java getPath servlet
python add_keyword.py java getDomain servlet
python add_keyword.py java getComment servlet
python add_keyword.py java getMethod servlet
python add_keyword.py java getPath servlet
python add_keyword.py java getReader servlet
python add_keyword.py java getRealPath servlet
python add_keyword.py java getRequestURI servlet
python add_keyword.py java getRequestURL servlet
python add_keyword.py java getServerName servlet
python add_keyword.py java getValue servlet
python add_keyword.py java getValueNames servlet
python add_keyword.py java getRequestedSessionId servlet

REM xss stuff
python add_keyword.py java javax.servlet.ServletOutputStream.print xss
python add_keyword.py java javax.servlet.jsp.JspWriter.print xss
python add_keyword.py java java.io.PrintWriter.print xss

REM response splitting stuff
python add_keyword.py java javax.servlet.http.HttpServletResponse.sendRedirect response_splitting
python add_keyword.py java addHeader response_splitting
python add_keyword.py java setHeader response_splitting

REM redirection stuff
python add_keyword.py java sendRedirect redirection
python add_keyword.py java setStatus redirection
python add_keyword.py java addHeader redirection
python add_keyword.py java setHeader redirection

REM sql and database stuff
python add_keyword.py java jdbc sql_and_db
python add_keyword.py java executeQuery sql_and_db
python add_keyword.py java select sql_and_db
python add_keyword.py java insert sql_and_db
python add_keyword.py java update sql_and_db
python add_keyword.py java delete sql_and_db
python add_keyword.py java execute sql_and_db
python add_keyword.py java executestatement sql_and_db
python add_keyword.py java createStatement sql_and_db
python add_keyword.py java java.sql.ResultSet.getString sql_and_db
python add_keyword.py java java.sql.ResultSet.getObject sql_and_db
python add_keyword.py java java.sql.Statement.executeUpdate sql_and_db
python add_keyword.py java java.sql.Statement.executeQuery sql_and_db
python add_keyword.py java java.sql.Statement.execute sql_and_db
python add_keyword.py java java.sql.Statement.addBatch sql_and_db
python add_keyword.py java java.sql.Connection.prepareStatement sql_and_db
python add_keyword.py java java.sql.Connection.prepareCall sql_and_db

REM ssl stuff
python add_keyword.py java com.sun.net.ssl ssl
python add_keyword.py java SSLContext ssl
python add_keyword.py java SslContext ssl
python add_keyword.py java SSLSocketFactory ssl
python add_keyword.py java SslSocketFactory ssl
python add_keyword.py java TrustManagerFactory ssl
python add_keyword.py java HttpsURLConnection ssl
python add_keyword.py java KeyManagerFactory ssl

REM session mgt stuff
python add_keyword.py java getSession session_mgt
python add_keyword.py java invalidate session_mgt
python add_keyword.py java getId session_mgt

REM legacy_interaction
python add_keyword.py java java.lang.Runtime.exec legacy_interaction
python add_keyword.py java java.lang.Runtime.getRuntime legacy_interaction

REM logging
python add_keyword.py java java.io.PrintStream.write logging
python add_keyword.py java log4j logging
python add_keyword.py java jLo logging
python add_keyword.py java Lumberjack logging
python add_keyword.py java MonoLog logging
python add_keyword.py java qflog logging
python add_keyword.py java just4log logging
python add_keyword.py java log4Ant logging
python add_keyword.py java JDLabAgent logging

REM architectural_analysis
python add_keyword.py java XMLHTTP architectural_analysis
python add_keyword.py java org.hibernate architectural_analysis
python add_keyword.py java org.apache.struts architectural_analysis
python add_keyword.py java org.exolab.castor architectural_analysis
python add_keyword.py java org.springframework architectural_analysis
python add_keyword.py java javax.xml architectural_analysis
python add_keyword.py java javax.faces architectural_analysis
python add_keyword.py java JMS architectural_analysis

REM generic
python add_keyword.py java Hack generic
python add_keyword.py java hack generic
python add_keyword.py java Kludge generic
python add_keyword.py java kludge generic
python add_keyword.py java Bypass generic
python add_keyword.py java bypass generic
python add_keyword.py java Steal generic
python add_keyword.py java steal generic
python add_keyword.py java Stolen generic
python add_keyword.py java stolen generic
python add_keyword.py java Divert generic
python add_keyword.py java divert generic
python add_keyword.py java Broke generic
python add_keyword.py java broke generic
python add_keyword.py java Trick generic
python add_keyword.py java trick generic
python add_keyword.py java FIXME generic
python add_keyword.py java fixme generic
python add_keyword.py java Fixme generic
python add_keyword.py java ToDo generic
python add_keyword.py java todo generic
python add_keyword.py java TODO generic
python add_keyword.py java Password generic
python add_keyword.py java password generic
python add_keyword.py java Backdoor generic
python add_keyword.py java backdoor generic

REM web2.0
python add_keyword.py java document.write web2.0
python add_keyword.py java eval web2.0
python add_keyword.py java document.cookie web2.0
python add_keyword.py java window.location web2.0
python add_keyword.py java document.URL web2.0

REM xmlhttp
python add_keyword.py java window.createRequest xmlhttp
