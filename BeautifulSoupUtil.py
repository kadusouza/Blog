def decomposeDivAvatarImageContainer(soup):
    for div in soup.find_all("div", {'class': 'avatar-image-container'}):
        div.decompose()
    return soup

def decomposePCommentContent(soup):
    for div in soup.find_all("p", {'class': 'comment-content'}):
        div.decompose()
    return soup

def decomposeSpanCommentactionsSecondaryText(soup):
    for div in soup.find_all("span", {'class': 'comment-actions secondary-text'}):
        div.decompose()
    return soup

def decomposeSpanIconUser(soup):
    for div in soup.find_all("span", {'class': 'icon user'}):
        div.decompose()
    return soup

def decomposeDivCommentReplies(soup):
    for div in soup.find_all("div", {'class': 'comment-replies'}):
        div.decompose()
    return soup

def decomposeSpanDatetimeSecondaryText(soup):
    for div in soup.find_all("span", {'class': 'datetime secondary-text'}):
        div.decompose()
    return soup

def decomposeDivCommentReplyBoxSingle(soup):
    for div in soup.find_all("div", {'class': 'comment-replybox-single'}):
        div.decompose()
    return soup

def decomposeSpanThreadToggleThreadExpanded(soup):
    for div in soup.find_all("span", {'class': 'thread-toggle thread-expanded'}):
        div.decompose()
    return soup

def decomposeDivContinue(soup):
    for div in soup.find_all("div", {'class': 'continue'}):
        div.decompose()
    return soup

def decomposePCommentFooter(soup):
    for div in soup.find_all("p", {'class': 'comment-footer'}):
        div.decompose()
    return soup

