from parser import find_emails

sample_inputs = [
    """
    This is a long string
    without an email address
    It is what it is
    """,


    """
    This string has an email!
    karl@erik.no
    (don't expect replies!)
    """,
    
    """
    Here is an email:simon@funke.no. It's probably not going to work.
    You could try funsim@uio.no, but I don't think that's the right one either. 
    """,

    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>
    """,

    """This is text which contains some email-like strings which aren't emails 
    according to the definition of the assignment:
    the string name@server.1o has a number at the start of thedomain,
    the string name@server.o1 has a number at the end,
    the string name@ser<ver.domin has an illegal character in its server,
    as does the string name@ser"ver.domain,

    however, the string na&me@domain.com is actually an email!
    as is n~ame@dom_ain.com
    but name@domain._com is bad
    (name@domain.c_o.uk is allowed though)
    """
]

find_emails(sample_inputs)