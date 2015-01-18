<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/rss">
        <html>
            <body>
                <div id="channelInfo">
                    <xsl:element name="a">
                        <xsl:attribute name="href">
                            <xsl:value-of select="channel/link" />
                        </xsl:attribute>
                        <xsl:value-of select="channel/title" />
                    </xsl:element>
                    <xsl:element name="p">
                        Description: <xsl:value-of select="channel/description" />
                    </xsl:element>
                    <xsl:element name="p">
                        Managing editor: <xsl:value-of select="channel/managingEditor" />
                    </xsl:element>
                </div>
                <div class="feed">
                    <dl style="padding:10px">
                        <xsl:for-each select="channel/item">
                            <div style="border:1px dashed red; margin:5px; padding: 5px;">
                                <dd style="margin:0px">
                                    <xsl:element name="a">
                                        <xsl:attribute name="href">
                                            <xsl:value-of select="link"/>
                                        </xsl:attribute>
                                        <xsl:value-of select="title"/>
                                    </xsl:element>
                                </dd>
                                <dt>
                                    <xsl:value-of select="description" /><br />
                                    <span style="font-size: x-small">Date: <xsl:value-of select="pubDate" /></span><br />
                                    <span style="font-size: x-small">Guid: <xsl:element name="a">
                                        <xsl:attribute name="href">
                                            <xsl:value-of select="guid" />
                                        </xsl:attribute>
                                        <xsl:value-of select="guid" />
                                    </xsl:element>
                                </span>
                            </dt>
                        </div>
                    </xsl:for-each>
                </dl>
            </div>
        </body>
    </html>
</xsl:template>
</xsl:stylesheet>
<!-- using this as a guide: http://www.evagoras.com/2011/02/10/improving-an-xml-feed-display-through-css-and-xslt/ -->
