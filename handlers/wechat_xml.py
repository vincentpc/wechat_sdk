textResp = '<xml>\n\
                <ToUserName><![CDATA[%s]]></ToUserName>\n\
                <FromUserName><![CDATA[%s]]></FromUserName>\n\
                <CreateTime>%d</CreateTime>\n\
                <MsgType><![CDATA[text]]></MsgType>\n\
                <Content><![CDATA[%s]]></Content>\n\
                <FuncFlag>%d</FuncFlag>\n\
           </xml>'

musicResp = '<xml>\n\
                <ToUserName><![CDATA[%s]]></ToUserName>\n\
                <FromUserName><![CDATA[%s]]></FromUserName>\n\
                <CreateTime>%d</CreateTime>\n\
                <MsgType><![CDATA[music]]></MsgType>\n\
                <Music>\n\
                <Title><![CDATA[TITLE]]></Title>\n\
                <Description><![CDATA[DESCRIPTION]]></Description>\n\
                <MusicUrl><![CDATA[%s]]></MusicUrl>\n\
                <HQMusicUrl><![CDATA[%s]]></HQMusicUrl>\n\
                </Music>\n\
                <FuncFlag>%s</FuncFlag>\n\
           </xml>'
           
picItem = '<item>\n\
            <Title><![CDATA[%s]]></Title>\n\
            <Description><![CDATA[%s]]></Description>\n\
            <PicUrl><![CDATA[%s]]></PicUrl>\n\
            <Url><![CDATA[%s]]></Url>\n\
           </item>\n'

picResp = '<xml>\n\
            <ToUserName><![CDATA[%s]]></ToUserName>\n\
            <FromUserName><![CDATA[%s]]></FromUserName>\n\
            <CreateTime>%d</CreateTime>\n\
            <MsgType><![CDATA[news]]></MsgType>\n\
            <Content><![CDATA[%s]]></Content>\n\
            <ArticleCount>%d</ArticleCount>\n\
            <Articles>\n\
            %s\n\
            </Articles>\n\
            <FuncFlag>%d</FuncFlag>\n\
           </xml> '
