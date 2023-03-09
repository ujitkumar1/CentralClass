# -*- coding: utf-8 -*-

import os
import re

# Define the new footer that you want to replace with
new_footer = '''
<footer class="sticky-footer bg-gray-xxlight">
<div class="width-page large-down-padding-horz-medium padding-vert-large border-box">
<div class="padding-bottom-medium margin-bottom-large border-bottom border-gray-mid row vert-align-middle">
<a class="margin-right-xsmall flex" href="index.html">
<i class="icon-lettermark-charcoal relative icon-large" style="top: 2px;">
<span class="off-page">होमपेज</span>
</i>
</a>
<div class="text-2 inline-block color-charcoal">
                          होमपेज
 </div>
</div>
<nav class="row wrap xlarge-up-nowrap margin-bottom-medium">
<div class="row width-100 medium-up-width-4-5 xlarge-up-width-1-2">
<div class="width-100 large-up-width-1-3 border-box padding-right-medium margin-bottom-medium"><a class="inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline" href="subjects.html">विषय के आधार पर ब्राउज़ करें
              
                              </a>
<ul class="list-no-style text-2">
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="subject/cs.html">कंप्यूटर विज्ञान</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="subject/psychology.html">मनोविज्ञान</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="subject/cybersecurity.html">साइबर सुरक्षा</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="subject/health.html">स्वास्थ्य</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="subject/law.html">कानून</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="subject/accounting.html">लेखांकन</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="subject/web-development.html">वेब विकास</a>
</li>
</ul>
</div>
<div class="width-100 large-up-width-1-3 border-box padding-right-medium margin-bottom-medium"><a class="inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline" href="providers.html">प्रदाता द्वारा ब्राउज़ करें
              
                              </a>
<ul class="list-no-style text-2">
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="provider/coursera.html">कोर्सेरा</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="provider/edx.html">एडएक्स</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="provider/futurelearn.html">फ्यूचरलर्न</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="provider/udacity">उधम</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="provider/swayam.html">स्वयं</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="provider/udemy.html">उद्यमी</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="provider/linkedin-learning.html">लिंक्डइन लर्निंग</a>
</li>
</ul>
</div>
<div class="width-100 large-up-width-1-3 border-box padding-right-medium margin-bottom-medium"><a class="inline-block text-2 margin-bottom-xxsmall color-charcoal weight-bold border-bottom border-gray hover-no-underline" href="universities.html">विश्वविद्यालय द्वारा ब्राउज़ करें
              
                              </a>
<ul class="list-no-style text-2">
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="university/harvard.html">हार्वर्ड</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="university/stanford.html">स्टैनफोर्ड</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="university/gatech.html">जॉर्जिया टेक</a>
</li>
<li class="margin-vert-xxsmall"><a class="color-charcoal" href="university/umich.html">मिशिगन विश्वविद्यालय</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="university/purdue.html">पर्ड्यू विश्वविद्यालय</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="university/duke.html">ड्यूक विश्वविद्यालय</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="university/iitm.html">आईआईटी मद्रास</a>
</li>
</ul>
</div>
</div>
<div class="row width-100 medium-up-width-3-5 xlarge-up-width-1-2">
<div class="width-100 large-up-width-2-5 border-box padding-right-medium margin-bottom-medium"><a class="inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline" href="institutions.html">संस्था द्वारा ब्राउज़ करें
              
                              </a>
<ul class="list-no-style text-2">
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="institution/google.html">गूगल</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="institution/microsoft.html">माइक्रोसॉफ़्ट</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="institution/ibm.html">आईबीएम</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="institution/amazon.html">अमेज़न</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="institution/linuxfoundation.html">लिनक्स फाउंडेशन</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="institution/british-council.html">ब्रिटिश काउंसिल</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="institution/salesforce.html">सेल्सफोर्स</a>
</li>
</ul>
</div>
<div class="width-100 large-up-width-3-5 margin-bottom-small">
<a class="inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline" href="rankings.html">
                रैंकिंग
              </a>
<ul class="list-no-style text-2">
<li class="margin-vert-xxsmall"><a class="color-charcoal" href="collection/top-free-online-courses.html">सभी समय के सर्वश्रेष्ठ ऑनलाइन पाठ्यक्रम</a>
</li>
<li class="margin-vert-xxsmall"><a class="color-charcoal" href="report/best-free-online-courses-2022/index.html">वर्ष के सर्वश्रेष्ठ ऑनलाइन पाठ्यक्रम</a>
</li>
<li class="margin-vert-xxsmall"><a class="color-charcoal" href="report/most-popular-online-courses/index.html">सभी समय के सबसे लोकप्रिय पाठ्यक्रम</a>
</li>
<li class="margin-vert-xxsmall"><a class="color-charcoal" href="report/most-popular-courses-2023/index.html">वर्ष के सबसे लोकप्रिय पाठ्यक्रम</a>
</li>
<li class="margin-vert-xxsmall"><a class="color-charcoal" href="report/coursera-top-courses/index.html">सभी समय के 250 शीर्ष मुफ्त कोर्सेरा पाठ्यक्रम</a>
</li>
<li class="margin-vert-xxsmall">
<a class="color-charcoal" href="report/edx-top-courses/index.html">100 सभी समय के शीर्ष मुफ्त edX पाठ्यक्रम</a>
</li>
<li class="margin-vert-xxsmall"><a class="color-charcoal" href="report/udemy-top-courses/index.html">सभी समय के 250 शीर्ष उदमी पाठ्यक्रम</a>
</li>
</ul>
</div>
</div>
</nav>
<div class="row margin-bottom-large">
<div class="row width-100 xlarge-up-width-1-2 horz-align-left">
<div class="width-100 large-up-width-1-3 xlarge-up-width-1-2 border-box padding-right-medium margin-bottom-medium">
<a class="inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline" href="report/index.html">
                कक्षा केंद्रीय
              आरएसएस फ़ीड द्वारा                <i class="relative inline-block symbol-report" style="width: 80px; top: 1px;"></i> रिपोर्ट</a> <a class="margin-left-xxsmall icon-center icon-small icon-rss-charcoal" href="report/feed/index.html">
</a>
<ul class="row list-no-style text-2">
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box">
<a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;The &quot;New Normal&quot; that Wasn't&quot;}" href="report/2022-year-in-review/index.html" title="&quot;नया सामान्य&quot; जो नहीं था">"नया सामान्य" जो नहीं था</a>
</li>
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box">
<a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;DDoS Attack on Class Central&quot;}" href="report/class-central-ddos-attack/index.html" title="डीडीओएस पर हमला">डीडीओएस पर हमला</a>
</li>
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box"><a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;500+ Online Degrees in India&quot;}" href="report/india-online-degrees/index.html" title="भारत में 500+ ऑनलाइन डिग्री">भारत में 500+ ऑनलाइन डिग्री</a>
</li>
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box">
<a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;Harvard's CS50 Free Certificate Guide&quot;}" href="report/cs50-free-certificate/index.html" title="हार्वर्ड के CS50 नि: शुल्क प्रमाणपत्र गाइड">हार्वर्ड के CS50 नि: शुल्क प्रमाणपत्र गाइड</a>
</li>
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box"><a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;How खुला विश्वविद्यालय Works&quot;}" href="report/open-university-insiders-perspective/index.html" title="खुला विश्वविद्यालय कैसे काम करता है">खुला विश्वविद्यालय कैसे काम करता है</a>
</li>
</ul>
</div>
<div class="width-100 large-up-width-1-3 xlarge-up-width-1-2 border-box padding-right-medium margin-bottom-medium">
<a class="inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;Free Courses and Certificates&quot;}" href="report/free-certificates/index.html" title="नि: शुल्क पाठ्यक्रम और प्रमाण पत्र">नि: शुल्क प्रमाण पत्र और पाठ्यक्रम</a>
<ul class="row list-no-style text-2">
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box">
<a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;700+ Free गूगल Certificates&quot;}" href="report/google-free-certificates/index.html" title="700+ निशुल्क गूगल प्रमाणपत्र">700+ निशुल्क गूगल प्रमाणपत्र</a>
</li>
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box">
<a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;Free LinkedIn Learning Certificates&quot;}" href="report/linkedin-learning-free-learning-paths/index.html" title="मुफ्त लिंक्डइन लर्निंग प्रमाण पत्र">मुफ्त लिंक्डइन लर्निंग प्रमाण पत्र</a>
</li>
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box">
<a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;1700 Free कोर्सेरा Courses&quot;}" href="report/coursera-free-online-courses/index.html" title="1700 नि: शुल्क पाठ्यक्रम">1700 नि: शुल्क पाठ्यक्रम</a>
</li>
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box">
<a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;Ivy League Online Courses&quot;}" href="collection/ivy-league-moocs/index.html" title="आइवी लीग ऑनलाइन पाठ्यक्रम">आइवी लीग ऑनलाइन पाठ्यक्रम</a>
</li>
<li class="width-100 margin-vert-xxsmall padding-right-xsmall border-box">
<a class="color-charcoal" data-track-click="footer_click" data-track-props="{&quot;type&quot;: &quot;Quick Links&quot;, &quot;title&quot;: &quot;175+ Free Writing Online Courses&quot;}" href="report/writing-free-online-courses/index.html" title="175+ नि: शुल्क लेखन ऑनलाइन पाठ्यक्रम">175+ नि: शुल्क लेखन ऑनलाइन पाठ्यक्रम</a>
</li>
</ul>
</div>
</div>
<div class="row width-100 xlarge-up-width-1-2">
<div class="width-100 medium-up-width-3-5 margin-bottom-medium">
<a class="inline-block margin-bottom-xxsmall text-2 color-charcoal weight-bold border-bottom border-gray hover-no-underline" href="about.html">
                क्लास सेंट्रल के बारे में
              </a>
<p class="text-2">कई प्रदाताओं से कक्षा केंद्रीय कुल पाठ्यक्रम आपको लगभग किसी भी विषय पर सर्वोत्तम पाठ्यक्रम खोजने में मदद करने के लिए, जहां भी वे मौजूद हैं।</p>
<ul class="margin-vert-medium list-no-style list-inline">
<li class="margin-right-xxsmall"><a class="icon-center icon-facebook-charcoal icon-medium" href="https://www.facebook.com/classcentral" rel="noopener" target="_blank"> </a>फेसबुक</li>
<li class="margin-horz-xxsmall"><a class="icon-center icon-twitter-charcoal icon-medium" href="https://www.twitter.com/classcentral" rel="noopener" target="_blank"> </a>ट्विटर</li>
<li class="margin-horz-xxsmall"><a class="icon-center icon-linkedin-charcoal icon-medium" href="https://www.linkedin.com/company/classcentral" rel="noopener" target="_blank"></a>लिंक्डइन
 </li>
<li class="margin-horz-xxsmall"><a class="icon-center icon-youtube-charcoal icon-medium" href="https://www.youtube.com/classcentral" rel="noopener" target="_blank"> </a>यूट्यूब</li>
</ul>
</div>
</div>
</div>
<div class="large-up-row vert-align-middle large-up-horz-align-left border-top border-gray-mid padding-top-medium">
<p>क्लास सेंट्रल © 2011 -2023 <a class="color-charcoal block large-up-inline-block large-up-margin-left-xsmall" href="about/privacy-policy.html">गोपनीयता नीति</a></p>
<ul class="list-no-style list-inline large-up-horz-align-right">
<li class="block large-up-inline-block large-up-padding-horz-small"><a class="color-charcoal" href="about.html">हमारे बारे में</a>
</li>
<li class="block large-up-inline-block large-up-padding-horz-small"><a class="color-charcoal" href="about/careers.html">हमसे जुड़ें</a>
</li>
<li class="block large-up-inline-block large-up-padding-horz-small">
<a class="color-charcoal" href="https://www.classcentral.com/help">सहायता केंद्र</a>
</li>
<li class="block large-up-inline-block large-up-padding-horz-small">
<a class="color-charcoal" href="contact.html">हमसे संपर्क करें</a>
</li>
</ul>
</div>
</div>
</footer>
'''

# Define the regular expression for the footer tag
footer_regex = re.compile(r'<footer class="sticky-footer bg-gray-xxlight">.*<\/footer>', re.DOTALL)

# Define a function to replace the footer tag in a single file
def replace_footer_in_file(filename):
    # Open the file for reading
    with open(filename, "r",encoding="utf-8") as f:
        contents = f.read()
    
    # Replace the footer tag with the new footer
    new_contents = footer_regex.sub(new_footer, contents)
    
    # Open the file for writing and write the new contents
    with open(filename, "w",encoding="utf-8") as f:
        f.write(new_contents)

# Traverse all the .html files in the current directory and its subdirectories
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if name.endswith(".html"):
            # Get the full path of the file
            filename = os.path.join(root, name)
            
            # Replace the footer in the file
            replace_footer_in_file(filename)
            
            # Print a message to indicate that the footer has been replaced
            print(f"Replaced footer in {filename}")
            
            # Print the file contents to check the replacement
            with open(filename, "r",encoding="utf-8") as f:
                print(f.read())
