# AppBlog

## 项目简介
这是一个基于Django的个人博客系统，主要用于记录个人学习以及生活

## 笔记部分

### Django日志
Django 使用 Python 内置的 logging 模块处理系统日志。

#### 日志框架的组成元素
一份 Python logging 配置有下面四个部分组成：
- Loggers
- Handlers
- 过滤器
- Formatters

##### Loggers
logger 是日志系统的入口。每个 logger 都是命名了的 bucket， 消息写入 bucket 以便进一步处理。

logger 可以配置 日志级别。日志级别描述了由该 logger 处理的消息的严重性。Python 定义了下面几种日志级别：

- DEBUG：排查故障时使用的低级别系统信息
- INFO：一般的系统信息
- WARNING：描述系统发生了一些小问题的信息
- ERROR：描述系统发生了大问题的信息
- CRITICAL：描述系统发生严重问题的信息
每一条写入 logger 的消息都是一条 日志记录。每一条日志记录也包含 日志级别，代表对应消息的严重程度。日志记录还包含有用的元数据，来描述被记录了日志的事件细节，例如堆栈跟踪或者错误码。

当 logger 处理一条消息时，会将自己的日志级别和这条消息的日志级别做对比。如果消息的日志级别匹配或者高于 logger 的日志级别，它就会被进一步处理。否则这条消息就会被忽略掉。

当 logger 确定了一条消息需要处理之后，会把它传给 Handler。

##### Handlers
Handler 是决定如何处理 logger 中每一条消息的引擎。它描述特定的日志行为，比如把消息输出到屏幕、文件或网络 socket。

和 logger 一样，handler 也有日志级别的概念。如果一条日志记录的级别不匹配或者低于 handler 的日志级别，对应的消息会被 handler 忽略。

一个 logger 可以有多个 handler，每一个 handler 可以有不同的日志级别。这样就可以根据消息的重要性不同，来提供不同格式的输出。例如，你可以添加一个 handler 把 ERROR 和 CRITICAL 消息发到寻呼机，再添加另一个 handler 把所有的消息（包括 ERROR 和 CRITICAL 消息）保存到文件里以便日后分析。

##### 过滤器
在日志记录从 logger 传到 handler 的过程中，使用 Filter 来做额外的控制。

默认情况下，只要级别匹配，任何日志消息都会被处理。不过，也可以通过添加 filter 来给日志处理的过程增加额外条件。例如，可以添加一个 filter 只允许某个特定来源的 ERROR 消息输出。

Filter 还被用来在日志输出之前对日志记录做修改。例如，可以写一个 filter，当满足一定条件时，把日志记录从 ERROR 降到 WARNING 级别。

Filter 在 logger 和 handler 中都可以添加；多个 filter 可以链接起来使用，来做多重过滤操作。

##### Formatters
日志记录最终是需要以文本来呈现的。Formatter 描述了文本的格式。一个 formatter 通常由包含 LogRecord attributes 的 Python 格式化字符串组成，不过你也可以为特定的格式来配置自定义的 formatter。

```
#管理员邮箱
ADMINS = (
    ('laixintao','*******@163.com'),
)

#非空链接，却发生404错误，发送通知MANAGERS
SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

#Email设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST= 'smtp.163.com'#QQ邮箱SMTP服务器(邮箱需要开通SMTP服务)
EMAIL_PORT= 25		   #QQ邮箱SMTP服务端口
EMAIL_HOST_USER = '**********@163.com'  #我的邮箱帐号
EMAIL_HOST_PASSWORD = '**************' #授权码
EMAIL_SUBJECT_PREFIX = 'website' #为邮件标题的前缀,默认是'[django]'
EMAIL_USE_TLS = True #开启安全链接
DEFAULT_FROM_EMAIL = SERVER_EMAIL = EMAIL_HOST_USER #设置发件人

#logging日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {#日志格式
       'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {#过滤器
        'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            }
    },
    'handlers': {#处理器
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {#发送邮件通知管理员
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],# 仅当 DEBUG = False 时才发送邮件
            'include_html': True,
        },
        'debug': {#记录到日志文件(需要创建对应的目录，否则会出错)
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "log",'debug.log'),#日志输出文件
            'maxBytes':1024*1024*5,#文件大小
            'backupCount': 5,#备份份数
            'formatter':'standard',#使用哪种formatters日志格式
        },
        'console':{#输出到控制台
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {#logging管理器
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['debug','mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}
```
以上的配置文件中，有三个日志处理器。分别是：

1.‘django.request’：django的request发生error会自动记录，然后使用debug将信息记录到文件，还有mail_admins将信息通过邮件发送给管理员。这里邮件的功能非常棒！并不是一个纯文本信息，而是一个html文件，和我们在浏览器看到的错误页面一模一样！要正常使用邮件功能需要像我一样配置一下上面的邮件发件人信息。我是直接去网易申请了一个邮箱。要格外注意三点：1.一定要去邮件服务商开启SMTP服务；2.不同的邮件服务商可能有一些特殊的设置，比如网易，会给你一个客户端授权码，这个才是密码，而不是网页的登录密码。3 注意服务商有没有对发信频率的限制。
2.‘django’：使用console处理器，将信息输出。在开发的时候就可以使用这个处理器（什么？print？ 太low了！）
3.最后一个处理器见注释。

最后，不要忘了给日志的路径响应的权限。比如Apache2服务器，就需要给www-data写权限：
```
sudo chown -R [yourname]:www-data [log]
sudo chmod -R g+s [log]
```