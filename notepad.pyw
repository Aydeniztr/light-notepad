
############## configuration ###############

titlebar_fg="#272727"
titlebar_bg="lightgrey"
titlebar_font=("calibri",10)
titlebar_bd=2

statusbar_fg="#272727"
statusbar_bg="white"
statusbar_font=("calibri",10)
statusbar_bd=2

menubar_font=("calibri",10)
menubar_activebackground="skyblue"

menuspecs_fg="#272727"
menuspecs_bg="white"
menuspecs_font=("calibri",10)
menuspecs_activebackground="skyblue"

txtarea_fg="lightgreen"
txtarea_bg="#093145"
txtarea_font=("Fixedsys",10)
txtarea_cursor_color="#dcdcde"

uploading_destination="https://0x0.st"

############################################

# Importing Required libraries & Modules

from os import getcwd
from os import system
from os import remove
from os import execl
from os import path
from os import name
from sys import executable
from sys import argv
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Label
from tkinter import Button

LICENSE = '''

                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    light-notepad  Copyright (C) 2022 Ahmet Yigit AYDENIZ
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.

'''

encoded_icon = '''
AAABAAEAgIAAAAEAIAAoCAEAFgAAACgAAACAAAAA
AAEAAAEAIAAAAAAAAAABABILAAASCwAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAABwcHAQcHBwEHBwcB
BwcHAgcHBwIHBwcDBwcHAwcHBwQHBwcEBwcHBAcH
BwUHBwcFBwcHBgcHBwYHBwcGBwcHBQcHBwQHBwcD
BwcHAgcHBwEHBwcBBwcHAgcHBwQHBwcEBwcHBQcH
BwUHBwcEBwcHBAcHBwMHBwcCBwcHAQcHBwEAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAcHBwEHBwcBBwcHAQcHBwIHBwcCBwcHAwcH
BwMHBwcEBwcHBAcHBwQHBwcFBwcHBQcHBwYHBwcG
BwcHBwcHBwcHBwcHBwcHCAcHBwkHBwcKBwcHCgcH
BwsHBwcMBwcHDQcHBw0HBwcOBwcHEAcHBxAHBwcR
BwcHEgcHBxMHBwcUBwcHFAcHBxMHBwcRBwcHDgcH
BwoHBwcHBwcHBwcHBwcHBwcKBwcHDQcHBxAHBwcS
BwcHEgcHBxEHBwcQBwcHDgcHBw0HBwcKBwcHCgcH
BwgHBwcHBwcHBgcHBwUHBwcEBwcHBAcHBwMHBwcB
BwcHAQcHBwEAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAHBwcBBwcHAQcHBwIHBwcDBwcHBAcHBwQHBwcE
BwcHBQcHBwUHBwcGBwcHBgcHBwcHBwcHBwcHBwcH
BwgHBwcJBwcHCgcHBwoHBwcLBwcHDAcHBw0HBwcN
BwcHDgcHBxAHBwcQBwcHEQcHBxIHBwcTBwcHFAcH
BxUHBwcVBwcHFgcHBxYHBwcYBwcHGQcHBxkHBwcb
BwcHHAcHBx0HBwcfBwcHIAcHByIHBwciBwcHJAcH
ByUHBwcnBwcHKAcHByoHBwcpBwcHKAcHByUHBwcf
BwcHGQcHBxUHBwcTBwcHFQcHBxkHBwcfBwcHIwcH
ByYHBwcnBwcHJQcHByMHBwchBwcHHgcHBxwHBwcZ
BwcHGAcHBxYHBwcUBwcHEwcHBxEHBwcPBwcHDQcH
BwwHBwcKBwcHCQcHBwcHBwcHBwcHBgcHBwQHBwcE
BwcHAwcHBwIHBwcBBwcHAQAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcB
BwcHAwcHBwUHBwcIBwcHCgcHBw0HBwcPBwcHEAcH
BxEHBwcSBwcHEwcHBxMHBwcUBwcHFQcHBxYHBwcW
BwcHGAcHBxkHBwcaBwcHGwcHBxwHBwcdBwcHHwcH
ByAHBwciBwcHIgcHByQHBwclBwcHJwcHBygHBwcq
BwcHKwcHBysHBwctBwcHLgcHBy8HBwcwBwcHMgcH
BzQHBwc1BwcHNwcHBzgHBwc6BwcHPAcHBz4HBwdA
BwcHQgcHB0MHBwdFBwcHRwcHB0YHBwdEBwcHQAcH
BzgHBwcwBwcHKgcHBygHBwcpBwcHMAcHBzcHBwc+
BwcHQgcHB0MHBwdCBwcHPwcHBzsHBwc4BwcHNAcH
BzEHBwcvBwcHLAcHByoHBwcoBwcHJQcHByIHBwcf
BwcHHQcHBxsHBwcZBwcHFwcHBxUHBwcTBwcHEgcH
BxAHBwcOBwcHDQcHBwsHBwcKBwcHCAcHBwcHBwcG
BwcHBQcHBwQHBwcEBwcHAwcHBwIHBwcBBwcHAQAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwcHAQcH
BwQHBwcIBwcHDQcHBxMHBwcZBwcHHgcHByIHBwck
BwcHJQcHByYHBwcoBwcHKQcHByoHBwcrBwcHLAcH
By4HBwcvBwcHMAcHBzIHBwc0BwcHNQcHBzcHBwc4
BwcHOgcHBzwHBwc+BwcHQAcHB0EHBwdDBwcHRQcH
B0cHBwdIBwcHSQcHB0sHBwdMBwcHTgcHB08HBwdS
BwcHUwcHB1UHBwdYBwcHWgcHB1wHBwdeBwcHYQcH
B2MHBwdlBwcHZwcHB2oHBwdsBwcHbAcHB2kHBwdj
BwcHWQcHB04HBwdGBwcHQwcHB0YHBwdOBwcHWAcH
B2EHBwdmBwcHZwcHB2UHBwdhBwcHXQcHB1kHBwdV
BwcHUgcHB04HBwdLBwcHRwcHB0QHBwdABwcHPQcH
BzoHBwc2BwcHMwcHBzEHBwcuBwcHKwcHBygHBwcm
BwcHJAcHByEHBwcfBwcHHAcHBxoHBwcYBwcHFgcH
BxQHBwcTBwcHEQcHBw8HBwcNBwcHDAcHBwoHBwcJ
BwcHBwcHBwcHBwcGBwcHBQcHBwQHBwcDBwcHAgcH
BwEHBwcBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcD
BwcHCAcHBxAHBwcZBwcHJQcHBy4HBwc2BwcHPAcH
Bz8HBwdBBwcHQwcHB0UHBwdGBwcHSAcHB0kHBwdL
BwcHTAcHB04HBwdPBwcHUgcHB1MHBwdVBwcHWAcH
B1oHBwdcBwcHXgcHB2EHBwdjBwcHZQcHB2cHBwdq
BwcHbAcHB20HBwdvBwcHcQcHB3IHBwdzBwcHdQcH
B3YHBwd4BwcHeQcHB3wHBwd9BwcHfwcHB4EHBweC
BwcHhQcHB4YHBweIBwcHigcHB4sHBweLBwcHiAcH
B4IHBwd5BwcHbQcHB2YHBwdjBwcHZgcHB24HBwd5
BwcHgQcHB4YHBweIBwcHhwcHB4QHBweABwcHfAcH
B3kHBwd2BwcHcwcHB3AHBwdsBwcHaAcHB2QHBwdg
BwcHWwcHB1cHBwdTBwcHTwcHB0wHBwdJBwcHRgcH
B0MHBwc/BwcHOwcHBzgHBwc0BwcHMgcHBy8HBwct
BwcHKgcHBygHBwclBwcHIgcHByAHBwcdBwcHGwcH
BxkHBwcXBwcHFQcHBxMHBwcSBwcHEAcHBw4HBwcN
BwcHCgcHBwgHBwcHBwcHBAcHBwIHBwcBAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwcHAQcH
BwUHBwcOBwcHGgcHByoHBwc7BwcHSgcHB1UHBwde
BwcHYgcHB2QHBwdnBwcHaQcHB2sHBwdtBwcHbwcH
B3AHBwdyBwcHcwcHB3UHBwd2BwcHeAcHB3oHBwd8
BwcHfQcHB38HBweBBwcHggcHB4UHBweGBwcHiAcH
B4oHBweLBwcHjQcHB44HBweQDAkIlhwUDqccFA6p
HBQOqSMXELMsGxLBLBsSwSwbEsM1IRXTPCQW3D0m
F9w+JhjdRi0b8EcuHPRILx30STAd9EEqGf87JRb/
GhINrQcHB5QHBweMBwcHhhEMCo4/JxbgQSoZ/0ow
HPJHLhzyPiYY3TgjFtkrGhLHJxgRvxsTDq8WDwum
BwcHlgcHB5QHBweRBwcHjgcHB4wHBweJBwcHhQcH
B4IHBwd/BwcHewcHB3gHBwd1BwcHcQcHB24HBwdq
BwcHZgcHB2IHBwdeBwcHWQcHB1UHBwdSBwcHTgcH
B0sHBwdIBwcHRAcHB0EHBwc9BwcHOgcHBzcHBwc0
BwcHMQcHBy4HBwcrBwcHKQcHByYHBwckBwcHIQcH
Bx8HBwcbBwcHFwcHBxMHBwcOBwcHCgcHBwYHBwcD
BwcHAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcB
BwcHCAcHBxUHBwclBwcHPAcHB1QHBwdnBwcHdQcH
B38HBweEBwcHhQcHB4gHBweJBwcHiwcHB4wHBweO
BwcHjw4KCZccFA6nHBQOqRwUDqkkGBC1LRwTwS0c
E8IsGxPDNyEV0jwlFts9KBfcPicY3UUtG/BHLhz0
SS8d9EswHfVELRv/RS0c/0YuHP9HLhz/SC8d/0gw
Hf9JMB7/SjEe/0syH/9MMyD/TjMg/080If9QNSH/
UTUi/1I2Iv9TNyP/VDgk/1Q4JP9VOST/Uzcj/0sy
H/82IhbYBwcHqQcHB6MOCwmmRy0c/U0yH/9TNyP/
VDgk/1M3I/9RNiL/TzQh/0wzIP9LMh//STAe/0cv
Hf9GLhz/SzAd/EgvHPRCKhnqPCUX3zAeE9ArGhLH
HxUOtRsTDq4LCQmbBwcHlQcHB5IHBweQBwcHjgcH
B4sHBweHBwcHhAcHB4AHBwd9BwcHeQcHB3YHBwdz
BwcHcAcHB20HBwdpBwcHZAcHB2AHBwdbBwcHWAcH
B1QHBwdQBwcHTAcHB0kHBwdGBwcHQwcHB0AHBwc8
BwcHOAcHBzQHBwcuBwcHJgcHBx4HBwcWBwcHDQcH
BwcHBwcDBwcHAQAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcH
BwIHBwcLBwcHGzomFm06JhaUNCIVpTwlF8Y+KRjU
PygZ2T8qGdpILxzuTDEe8E0xHvFOMh/ySzEd/0ow
Hv9KMR7/SjEf/0sxH/9NMh//TDIg/04yH/9OMyD/
TjQg/080If9QNSH/UTYi/1I2I/9TNyL/VDgj/1U5
JP9VOCT/Vjok/1c5Jf9XOiX/Vzol/1g6Jv9XOyb/
WDsm/1g7Jv9ZOyf/WTsn/1k7J/9aPCb/Wjwo/1s9
J/9bPSf/XD0o/1w+KP9dPij/XT4p/10/Kf9cPij/
WDsm/1E2Iv9KMR7/Ry8d/08zIO5SNyP/WTsn/1w+
KP9dPij/XD4o/1w9KP9bPCf/Wjwm/1k7J/9YOyb/
Vzsm/1Y6Jf9VOSX/VDgk/1I3I/9QNSL/TTQh/00y
H/9KMR7/SDAd/0YuHP9FLRv/SS8d9kcuHPQ+Jhjf
OiQW3CsbEscoGBHBGxMOrxcQDKcHBweWBwcHlAcH
B5EHBwePBwcHjAcHB4kHBweGBwcHggcHB38HBwd8
BwcHeAcHB3UHBwdyBwcHbgcHB2oHBwdnBwcHYgcH
B14HBwdZBwcHUwcHB0wHBwdABwcHNAcHByYHBwcY
BwcHDQcHBwYHBwcBAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BwcHBAcHBw4rHRM3TjIe/Fo7Jf9fPSj/Xz8o/18/
KP9fPyn/Xz8o/189Kf9ePSn/Xj4o/10/KP9ePij/
XT4o/108KP9cPif/XD0o/1w9J/9cPSf/Wz4p/1w9
KP9bPSf/XD0n/1w9KP9dPij/XD4o/10+Kf9dPyn/
Xj8o/2ZJNv9tVUL/bVZD/21VQv9tVUL/cV9N/3Ff
Tv9xXk3/cF5N/29eT/9tXU//bF5O/2xeTv9sXk7/
Z1tN/2dbTv9nWk3/Z1pN/2VZS/9jV0r/Y1dK/2pd
Tv9oUD3/WDsn/1I3I/9NNCH/TDMh/000If9QNSL/
W0U2/2FLOf9bPir/XT8p/14/Kf9ePyn/Xj8p/14/
Kf9ePyn/Xj8p/14/Kf9dPij/XD4o/1s9J/9aPCj/
WTsn/1g7J/9YOyb/Vzom/1Y6Jf9VOST/Uzkj/1E2
Iv9PNSH/TDMg/0syH/9JMB7/Ry8d/0YuHP9LMB39
SC8c9EMrGus7JxffMR8T0SsbEschFg+4GxMOrgwJ
CJwHBweVBwcHkwcHB5EHBweOBwcHiwcHB4gHBweE
BwcHgQcHB3wHBwd3BwcHbQcHB2AHBwdPBwcHOgcH
ByUHBwcVBwcHCgcHBwMAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAHBwcEBwcHEEouG5tePif/bEkw/3BMMv9vTDP/
bkwy/21KMf95X0j/e19L/3pgSv96X0v/fWZT/4Rv
Xv+Eb17/gm9d/4JsXf+EcmX/hHJk/4NxZP+BcGL/
f3Bi/3xvYv96a17/eGte/3ZoXP9vYlb/bWBU/2xg
U/9rX1L/al5R/2ldUP9oXE//aFxP/2dbTv9nW07/
ZlpN/2ZaTf9lWk3/ZVlM/2RYS/9kWEv/ZFhL/2JW
Sv9iVkr/YlVI/19TRv9dUUX/XFBE/1tPQ/9aT0P/
WE1B/1ZLP/9SRzz/UEU6/0EzJ/82JBn/MyQZ/zgq
H/84MSr/Pjgw/0xCOv9VSj//W1BE/15SRv9gVEj/
YlVI/2JVSP9iUkT/ZVRG/2VSQf9lTz3/Y0o4/1o8
KP9bPSn/XD4o/1w+KP9cPij/XD4o/1w9KP9cPSj/
XD0o/1s8J/9aPCb/WTsn/1g7Jv9XOyb/Vjol/1U5
Jf9UOCT/Ujcj/1E1Iv9PNCH/TDMg/0oxHv9IMB3/
Ry4c/0UtG/9IMB33Ry4c9T4nGOE7JBbdKxsSyCoa
EsMbEw6wGBEMqAcHB5QHBweLBwcHfAcHB2cHBwdP
BwcHMwcHBx4HBwcOBwcHBAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAcHBwQHBwcQTjIetGdFLf91UDT/eFM2/458
a/+Pg3j/j4N4/46Ddv+Ngnb/jYF2/4uBdP+JgHP/
iH5x/4d9cP+Fem3/hXhr/4J2af+AdGf/e25i/3dq
Xv9wZFn/a2BX/2tgVf9nXlP/Z1xR/2VaT/9jWE3/
YVZL/19USf9dUkf/XFFG/1xRRv9bUEX/WU5F/1pO
Q/9YTUL/WExB/1dMQf9XTEH/VUxB/1ZLQP9WS0D/
U0g//1FGPf9PRDv/TEI6/0g+N/9FOzT/Qjwy/0M8
Mv8/OC//Pzgv/19PQf+QgHH/pJeI/6qejf+wpJP/
r6OT/5qLff9AOTD/Miwn/zYwKf84Miv/PDQu/z44
Mf8/OTL/QDoz/0I7NP9CPDT/Rj02/0pBOf9NQzv/
T0U9/1JJPv9aTkP/W09D/11QRf9fUUX/YFBE/2JS
RP9jUkP/Ykw6/2JLOf9UOSX/VTom/1c7J/9aPCj/
XD4o/10+KP9cPij/Wz0n/1o8KP9ZOyf/WDsn/1g7
Jv9XOib/Vjol/1U5JP9TOCT/UjYi/1A1If9OMyD/
SzIf/0kwHv9GLhz/RCwb/zMgFNQMCQiWBwcHegcH
B14HBwc+BwcHJAcHBxEHBwcFAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAABwcHBAcHBxFRMyC0akcu/3dSNv+GaVL/
kYV5/5CEeP+Kf3T/gHVq/3dtZP92bWL/dGtg/3No
X/9xZ17/cGZd/3BmXv9vZVz/bmNa/2pgV/9lXFH/
XlRL/1NMQ/9QRz//T0g//05EPP9LQjr/SEE7/0c+
N/9CPDX/Pzky/z03MP89NzD/PTYv/zw1L/88NS7/
OjMt/zgyK/83MSv/NzAq/zcwKv83MSr/NzAq/zgy
LP9AOjL/SD42/0hANv9aTUD/b2BS/3ptXf+Lf2//
no6A/6ygkP+xpZX/tqqd/7isoP+1qp7/uK2g/7qu
ov+6rqL/ua2h/7ernv+zp5f/rqKS/6qekP+jlIb/
nI9//5mMe/+Jemf/eWpd/2ZbTf9YTEH/UUg9/0xC
Ov9GPTb/Qjsy/0I8NP9EOzT/Qzwz/0A6Mv8/ODH/
PTYw/z84Mf9COzL/Qzw1/0Q7NP9FPDX/SD43/09F
PP9aT0P/XVFG/15SR/9dUUb/X1NH/2FTSP9hU0f/
YlRI/2JUSP9iVUj/YVFC/2FRQv9iUEL/Y1JE/2lV
RP9jSzj/WDsm/1Y6Jf9TOSP/SDAd/z8mFvwHBweH
BwcHaQcHB0YHBwcpBwcHFAcHBwYAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAHBwcEBwcHEVE1IbRsSTD/eVM3/4dr
Vv+RhXn/kIN4/4F2a/9fWE//SkQ+/0hCPP9JQj3/
SkQ9/0lDPP9HQTv/R0E7/0lCPP9PRj//U0xC/1RN
Qv92Zlf/emtd/3dnW/93aFv/e21d/31uYf+BcGP/
koV2/6GUhP+kl4f/pJaG/6WXh/+klob/ppaH/6mc
jP+ypZX/sqaW/7Kmlv+ypZX/sqWW/7Kllv+yppX/
sqWU/7Cklv+topP/rqOS/7GlmP+1qp3/t6qe/7eq
n/+3rKH/uq6h/7quof+6r6L/uq6i/7esn/+4rKH/
ua2h/7quov+6raH/uq2h/7mtof+5raH/ua2g/7mt
oP+5raH/uq6i/76xpP+/sqP/vrGi/7ytoP+5rJ//
t6ib/7Ommf+vopX/qZ2P/6qdjf+pnIz/opOF/4t+
bf97a17/d2da/3VlWf9vYVX/al1R/11RRP9JQDj/
OTIr/zUuKP83MCr/NzAq/zcwKv83MCr/NjAp/zcw
Kv83MSr/ODIr/zgyK/84Miv/ODIr/zo0Lf9CPDT/
U0g//2teUf9ePyn/Xj8p/1w+KP9TNyP/Qysa/wcH
B44HBwdwBwcHSgcHBywHBwcWBwcHBwAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAcHBwQHBwcRUTUhtG1KMf96VTj/
iGxX/5KGef+RhXn/kH9q/7Kik/+0ppb/tKWX/7Wl
l/+2ppj/taWX/7Ollf+uoZH/rJ+O/6qfjv+xpJX/
uKqe/7utof+6raH/ua2h/7muof+7rqL/u6+i/7yv
o/+8saT/vbGk/7ywpP+8sKT/vLCk/7ywpP+7r6P/
vLCk/7uwo/+8r6T/vLCk/7ywpP+8sKP/vLCk/7uw
pP+7r6P/u6+j/7uvov+5rqL/uq+i/7uvo/+7rqP/
u6+j/7qvov+8r6P/u6+i/7uvov+6r6L/tqug/7it
oP+6rqH/ua2i/7quov+6raH/uq2h/7mtof+5raL/
ua2h/7mtof+5raD/ua2h/7mtof+5raH/ua2h/7mt
of+5raH/ua2h/7isoP+4rKD/ua2h/7mtof+5raD/
vLCj/76ypP+/s6P/vbKk/72xpP+8sKP/vK+g/7mq
nf+2p5r/sqaY/7Gll/+yppj/s6aX/7Oml/+zppf/
saWX/62ekP+sn5D/rJ+P/6ufj/+onI7/hXdn/0Q7
M/9DPDP/ZVlN/14/Kf9ePyn/Xj8p/1Y6Jf9JMB3+
BwcHkAcHB3EHBwdLBwcHLQcHBxYHBwcHAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAABwcHBAcHBxBSNSGzb0sx/3xX
OP+JbVj/koV6/5GFev+tnYv/yr2w/8q/sf/JvbD/
yLyu/8e7rf/Hu63/xbmr/8O2qf/Dtqf/wbao/8K2
qP/Ctqj/wrap/8G0p/+/s6f/wbSn/8C1p//As6b/
wLOn/7+zpf++sqX/vrKk/72ypf+9saX/vrKk/76y
pP+9saT/vbGk/7ywpP+9saT/vbGk/72wpP+9saT/
vLGk/7ywpP+8sKT/vLCj/7uwpP+8saT/vLCk/7yv
o/+8sKP/u6+j/7uvo/+6r6P/u7Cj/7uuo/+3rJ//
uKyg/7muov+6raL/uq6h/7quo/+5rqL/uq2h/7mt
of+5raH/ua2h/7mtof+5raH/ua2h/7mtof+5raH/
ua2h/7mtof+4rKD/uKyg/7isoP+4rKD/uKyg/7is
oP+4rKD/uKuf/7irn/+4rKD/uKyg/7isoP+3rKD/
t6yg/7esoP+4rKD/uKyg/7isoP+4rKD/uKyg/7ms
oP+4rKD/uKyg/7mtof+5raH/uayh/7mtoP+4q5//
iXxs/z44MP9iV0r/Xj8p/14/Kf9ePyn/Vjol/0gw
Hf4HBweQBwcHcAcHB0sHBwcsBwcHFgcHBwcAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAHBwcEBwcHEFI1IbNvSzL/
f1g5/4tvV/+RhXr/koZ6/6yejP/Lv7H/zMCy/8q+
sP/JvbD/yL2v/8e7rv/Huq3/xrqs/8W4q//DuKr/
w7er/8O3qf/Ctqn/wrao/8K1qP/Btqj/wbWn/8G0
p//Ataf/v7Om/7+zpv/As6f/v7Sm/7+zpf++s6X/
v7Ol/76zpf++sqT/vbGl/76ypf+9saX/vrKk/76y
pP+9saT/vLCk/76ypP+9saT/vbGl/72xpP+9saT/
vLCk/7ywpP+8saT/vK+j/7uwo/+7r6L/u66j/7is
of+5raH/u6+j/7uvo/+6r6L/u66i/7uvov+6rqP/
uq6i/7qtof+5raH/ua2h/7mtof+5raH/uq6h/7mt
of+4rKD/ua2h/7isoP+4rKD/uKyg/7isoP+4rKD/
uKyg/7isoP+5rKD/ua2g/7isoP+4rKD/uKyg/7ms
oP+5rKD/uayg/7isoP+4rKD/uKyg/7isoP+5rKD/
uKyg/7irn/+4rKD/ua2h/7mtof+5raH/ua2h/7mt
oP+Sg3X/Pjgw/2RYS/9ePyn/Xj8p/14/Kf9WOiX/
SS8e/QcHB48HBwdwBwcHSgcHBywHBwcWBwcHBwAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAcHBwQHBwcQUTQgpnBN
M/+AWDr/jG9a/5KGev+Shnr/rp+M/8zAsv/MwbT/
zMCy/8q/sf/JvrD/yL2v/8i8rv/Guq3/xbqs/8a5
rP/EuKr/xLiq/8K2qv/Ctqn/wrap/8O3qf/Ctqn/
wbWo/8G1p//AtKf/v7Sn/8C0pv/AtKf/v7Sm/7+z
pv++s6X/v7Om/76zp//As6f/v7Sm/7+zpf+/s6X/
v7Ol/76zpf++sqT/vrKm/76ypf++sqb/v7Ol/76y
pf+8sKT/vbGk/72xpP+9saT/vK+k/7ywpP+7r6P/
uKuf/7mtof+7r6P/uq+j/7qvov+7r6L/uq6i/7uu
ov+6raL/uq6j/7quov+6raH/ua2h/7isof+5raH/
ua2h/7mtof+4rKD/ua2h/7isoP+4rKD/uKyg/7is
oP+4rKD/uayg/7isn/+4rKD/uKyf/7isn/+4rKD/
tquf/7ern/+2q5//tquf/7arn/+3q5//uKyg/7ir
n/+4rKD/ua2g/7isoP+4rKD/uKyg/7isof+5raH/
uayg/5KDdf8+ODD/ZFhL/14/Kf9ePyn/Xj8p/1Y5
Jf9MMR37BwcHjgcHB3AHBwdKBwcHLAcHBxYHBwcH
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAABwcHBAcHBxBRNCGm
cE0z/4FaO/+Ka1T/koZ7/5KGev+rnoz/zcGz/83C
tP/MwLP/y7+y/8q/sf/JvbD/ybyw/8i8r//Hu63/
x7qt/8W5rP/Fuav/xLis/8S4qv/Dt6v/w7ep/8K2
qP/Btan/wrap/8G1p//Btaj/wbWo/8C0p//Ataf/
wbSn/8C0p//Ataf/v7Sn/8Czpv/AtKb/wLWn/7+0
pv+/s6b/v7Om/76zpv+/tKb/wLOn/7+0pv+/s6X/
v7Om/76ypP++sqX/v7Ol/72xpP+8sKT/vbGl/7uw
o/+4rKD/uq6i/7ywo/+8sKT/vLCj/7uvo/+7r6P/
vK+i/7uvov+6rqL/u66j/7quof+5raL/uq2h/7mt
of+4rKH/ua2g/7quof+5raH/ua2h/7isoP+4rKD/
uKuf/7isoP+5rKD/uKyg/7isn/+4rJ//t6uf/7es
n/+3q5//t6uf/7ern/+4q5//uKuf/7ern/+3q57/
t6yf/7arn/+4q5//uKyg/7esoP+4rKD/uKyg/7mt
of+4rJ//k4N1/z44MP9kWEv/Xj8p/14/Kf9ePyn/
VTkl/0swHfsHBweOBwcHbwcHB0kHBwcrBwcHFQcH
BwcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcEBwcHEFI0
IaVyTjT/gls8/4ttVP+Shnv/koZ7/6ycjP/Pw7X/
zsK2/83Dtf/MwbP/zMCz/8u/sv/KvrH/ybyv/8e7
rv/Hu67/xbqt/8a6rP/Fuaz/xrms/8S4q//Et6v/
xLiq/8O3qf/CuKr/wrep/8K3qf/Ct6r/wrap/8G3
qf/Ctqj/wrao/8G1p//Btqn/wbWo/8C0p//AtKf/
wban/8C1p//BtKf/wbWn/8C1p/+/tKf/wLSm/8C1
p/+/s6b/vrOm/8Czp//AtKb/v7Om/7+ypf++sqX/
vrKk/7mtof+7r6L/vLCj/72xpP+8r6T/vLGk/7yv
o/+8sKP/vK+j/7uvo/+8r6T/uq6i/7muov+6raL/
uq6j/7qtof+5raH/uKyh/7mtoP+5raH/uKyh/7is
oP+4rKD/uKyg/7msoP+4rKD/uKyf/7ern/+3q5//
t6uf/7ern/+3q5//t6ug/7arn/+2q5//t6uf/7er
n/+3qp//t6uf/7ern/+4rJ//uKyg/7esoP+4rKD/
ua2h/7isoP+Tg3b/Pjgw/2VXS/9ePyn/Xj8p/14/
Kf9VOSX/SjAe+gcHB44HBwduBwcHSQcHBysHBwcV
BwcHBwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcHBwQHBwcQ
UjQhpXRNNP+CXD7/jG5V/5SHfP+Shnv/rJ6M/8/E
tf/Qxbf/z8O2/83Ctf/MwrT/y8Cy/8zAsv/KvrH/
yb2w/8i8rv/Iu67/x7uu/8e7rf/Hu63/xrms/8W5
rP/Euaz/xbmr/8S4q//Dt6v/w7iq/8S4qv/Dt6r/
w7ep/8K2qv/Dt6n/wrep/8K3qf/Ctqn/wrep/8K2
qP/Ctqn/w7Wp/8K2qP/Ctqn/wrao/8G2qf/Btaj/
wLSn/8C1p//Btaf/v7Sm/8C0pv+/tKb/v7Om/76z
pf+/s6X/ua2h/7uvo/++sqT/vrKk/7ywpP++saT/
vbGk/7yvo/+8sKT/vK+j/7ywo/+7rqP/u6+j/7uu
ov+6rqL/ua2h/7quof+6rqL/uKyh/7isof+6rqH/
uKyh/7isoP+4rKD/uKyg/7mtoP+4q5//tquf/7er
nv+3q5//t6uf/7ern/+3q5//t6ue/7esn/+3rJ//
t6uf/7arn/+3q5//t6uf/7ern/+4rJ//uKyg/7is
oP+5raH/uKug/5ODdv8+ODD/ZVhJ/14/Kf9ePyn/
XT8p/1U5JP9JMB32BwcHjQcHB20HBwdIBwcHKwcH
BxUHBwcGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwcHBAcH
BxBSNSGldU81/4VePv+NblX/lIh8/5OHe/+sn4r/
0MW2/9DFuP/RxLf/zsO1/83Ctf/MwbT/zMCz/8u/
sf/JvrH/yb6w/8q9sP/Jva//yLyv/8i8rv/HvK7/
xrut/8a6rf/Fuqz/xrqs/8W6rP/Fuaz/xLmq/8a5
rP/Fuav/xbir/8W4q//EuKr/xLiq/8O3q//DuKr/
xLeq/8O3qf/Dt6r/w7ep/8K2qv/Dt6n/w7eq/8K2
qf/Ctqj/wbWo/8K2qP/Ctqj/wbWo/8C0p//Btaf/
wLSn/7+ypf+5rqH/vLCk/76zpv+/s6X/vrKl/76y
pf+/s6X/vbGk/72xpP+9saT/vK+k/7ywpP+8r6P/
u6+i/7qvov+6r6L/uq6h/7mto/+6rqP/uq6i/7mt
of+5raD/ua2h/7isoP+4rKD/uKyg/7isoP+4rJ//
t6uf/7ern/+3q5//t6uf/7ernv+3q57/t6ue/7er
nv+3q57/t6ue/7ern/+3q5//t6uf/7ern/+4q5//
uayg/7isoP+4rKD/k4V1/z44MP9lWUn/Xj8p/14/
Kf9dPin/VDgk/0gvHfYHBweMBwcHbQcHB0cHBwcq
BwcHFAcHBwYAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcE
BwcHEFI2IaV0UDb/hl5A/45vVv+UiH3/k4h8/6ye
jP/Sx7j/0sa5/9HGuP/PxLf/z8S2/87Ctf/NwrT/
zMGz/8u/sv/Lv7L/yb6w/8q+sf/KvrD/yLyv/8m9
r//Iva//x7yv/8e8rv/HvK7/xrut/8a6rP/Hu63/
xrqt/8e6q//Fuqz/xrms/8a6rP/Fuaz/xrqt/8W6
rP/Fuaz/xbmr/8S5rP/Fuav/xbmr/8W4q//EuKv/
xLiq/8O4qv/Dt6n/w7ep/8O3qf/Dt6n/wrao/8K2
qf/Ctqn/wbSo/7quov+8saT/wLWn/8C0pv/AtKb/
v7Sm/7+0pv+/sqX/vrKk/72xpf+9saT/vbGk/72x
pP+8r6P/vLCk/7uwo/+7rqP/u6+j/7uuo/+7raP/
uq6j/7qtof+4rKH/uq6h/7mtof+4rKD/uKyg/7is
oP+4rKD/t6yf/7ern/+2q5//t6yf/7ernv+3q57/
tqqe/7ernv+3q57/t6ue/7arn/+3qp//t6ue/7is
oP+4rKD/uKuf/7isof+ThHb/Pjgx/2ZXSv9ePyn/
Xj8p/10+KP9UOCT/SC8d9AcHB44HBwdwBwcHTAcH
By4HBwcYBwcHBwcHBwEAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcH
BwQHBwcQUzYhpHZSNv+HX0D/j3BX/5SIff+UiH3/
rZ2L/9PIuf/TyLv/08e6/9LGuP/Qxbj/z8S3/87E
tv/NwrX/zcG0/8zBtP/MwbL/zMCy/8u/sf/Lv7H/
yr6x/8m+sP/Jva//yr2w/8m8r//Iva7/yLyu/8i8
r//IvK//yLyu/8e6rv/Hu67/x7uu/8i7rv/Hu63/
xrqt/8e7rf/Guqz/x7ut/8a6rf/Guqz/xbqs/8a5
rP/Fuaz/xbqs/8W5q//Euaz/xbir/8S4qv/Et6v/
xLiq/8O3q//Ctqj/vK6j/7+zpv/Btqj/wrap/8C0
p//BtKf/v7Sn/8C0p/+/s6b/wLOn/76ypf++sqb/
v7Gl/72xpP+9saT/vbGk/7uwpP+8r6P/u6+j/7uv
o/+7rqL/u66i/7mtov+4raH/ua2g/7mtof+4rKD/
uKyg/7isoP+4rKD/t6ue/7ern/+3q5//t6ue/7er
nv+2qp7/tqqe/7aqnv+3q57/t6uf/7ern/+3q5//
tquf/7isoP+4rKD/uKyg/5ODdv8+ODH/ZldK/14/
Kf9ePyn/XT4o/1Q4JP9HLhzyBwcHlAcHB3kHBwdX
BwcHOwcHByEHBwcOBwcHBAcHBwEAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BwcHBAcHBxBTNiKkd1I2/4hgQf+Rclf/lIh8/5SI
ff+rm4z/08m6/9TKvP/TyLv/08i6/9HGuP/Qxbj/
0MO3/87Etv/NwrX/zcK1/83BtP/MwbP/zMCz/8zA
s//MwLL/zMCy/8zAsv/KvrL/yb6w/8q+sP/KvbD/
yr2w/8q+sP/KvrD/yb2v/8m9sP/IvK//yL2w/8m8
r//Iva7/yL2u/8i8rv/IvK//yLyv/8e7rv/Iu6z/
yLyu/8i8r//IvK7/x7ut/8e7rf/Guqz/x7qr/8a5
rP/Fuaz/xLms/8O3qv+8sKT/v7Sn/8O4qv/Dt6n/
wrap/8K2qf/Btaj/wbWo/8G0qP/AtKf/wLSn/7+z
pv/As6f/v7Ol/76ypv+/s6X/vLCk/72xpP+8sKT/
vK+k/7ywo/+7r6P/u66i/7qtov+6rqL/uayh/7mt
of+4raD/uKyg/7isoP+4rKD/t6uf/7ern/+3q5//
t6ue/7ernv+2qp7/t6ue/7ernv+3q5//t6uf/7er
n/+3q5//uKyg/7isoP+4rKD/k4N2/z44Mf9mV0r/
Xj8p/14/Kf9dPij/Uzgk/0YuG/IHBwecBwcHhwcH
B2wHBwdPBwcHMgcHBxgHBwcKBwcHAwAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAHBwcEBwcHEFM2IqR3Ujb/iWFA/5BxVf+ViH3/
lIh9/6mZif/Uybz/1sq9/9bKvv/Tybv/0si6/9LH
uf/Rxbj/0MW3/9DFt//Pw7b/zsK2/87Ctf/NwrX/
zcK0/83BtP/MwbP/zMGz/8zAs//MwLP/zMCy/8u/
sv/MwLP/y7+x/8u/sf/Lv7H/zMCy/8q+sv/Lv7H/
yb6w/8q/sf/KvrD/yr2w/8m9sP/JvrD/yruu/8m9
r//JvbD/yr2w/8q9sP/Jva//ybyw/8i8r//Iu67/
x7uu/8e7rf/Hu63/xbms/72xpP/Btaj/xbmr/8W4
q//EuKz/xbir/8O3q//Dt6r/wrao/8G1p//Btaf/
v7Om/76ypf+/s6f/v7Ol/8Czp/+/s6X/vbKl/76y
pP+9saT/vLCk/7yvpP+8sKP/uq+j/7quov+6rqP/
uq6h/7mtoP+5raH/uK2h/7iroP+4rKD/t6uf/7eq
n/+2q57/t6yf/7ernv+3q57/t6ue/7ern/+3q5//
t6uf/7arn/+4rKD/uKyg/7isoP+Tg3b/Pjgx/2ZW
Sf9ePyn/Xj8p/10+KP9TOSP/RCwb8QcHB6oHBwec
BwcHhwcHB20HBwdLBwcHJwcHBxEHBwcFAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAcHBwQHBwcQUTUhl3dTNv+JYEH/kG5T/5SJ
fv+UiX3/qZaE/9XJvP/YzMD/1su//9bKvf/Tybv/
08i6/9PHuv/Rxrn/0cW4/9DFt//PxLf/0MW2/8/E
t//Ow7X/zsS2/8/Dtf/Ow7X/zcK1/8zCtP/MwbT/
zcG0/83BtP/NwbT/zMGz/8zBsv/MwLP/zMG0/8zA
s//MwLP/zMCy/8zBsv/Lv7L/zMCy/8u/sv/Lv7L/
y7+x/8zAsv/LvrH/zL+w/8q+sP/KvrH/yr6x/8q+
sP/IvK//ybyv/8i8sP/Guq3/vrKl/8O3qf/Guq3/
xrqu/8a6rP/Guq3/xLms/8W5q//Dt6r/wbWo/7+z
pf+9sqT/vbCk/7+yp/+/s6b/wbSn/8G0p/+/s6b/
v7Sm/72ypP+9sqT/vLGk/72xpP+8r6T/u6+j/7yv
pP+7rqP/ua6i/7itof+5raL/uKyg/7esoP+4rJ//
t6yf/7eqn/+3q5//tquf/7ern/+3q5//t6uf/7eq
n/+3q57/uKyg/7isoP+4rKD/uKyg/5ODdv8/OTH/
ZldJ/14/Kf9ePyn/XD4o/1M3I/9FLBr+KBsS8DMl
GeM9Kx3VPiweuAcHB2MHBwc3BwcHGQcHBwgAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAABwcHBAcHBxBRNSGXeFQ3/4lhQv+Sb1L/
lYl+/5SIff+pl4X/18u+/9nOwf/YzMD/18y+/9bK
vf/Vyr3/1ci7/9PHuv/SyLr/0ca4/9HGuP/Rxrj/
0MW3/9DFuP/Qxbj/0MW3/9DFtv/PxLf/zsO2/87D
tf/Ow7b/zsS2/8/Dtv/Pw7X/zsK1/87Ctf/NwbX/
zcK1/8zCtP/NwrX/zMK0/83BtP/NwrT/zMCz/8zB
s//MwbP/zMGz/8zAs//MwLP/y7+y/8vAsv/LwLL/
y7+y/8q+sv/Kv7H/yr6x/8i8rv++sqX/w7ir/8m8
r//IvK//yLyu/8e7rv/Hu63/xbqs/8G1qP+9saT/
uK2h/7esof+4r6L/vLGk/7+zp//Ctaj/wrap/8G2
qP+/tKf/v7Sm/8C0p/+/s6b/vbGl/72wpP+9sKT/
vK+j/7uvo/+6rqL/uq6h/7mtof+4raH/ua2h/7is
oP+5rKD/tquf/7ernv+4q5//t6qf/7ern/+3qp//
t6uf/7ern/+4rJ//ua2h/7isoP+4rKD/k4N3/z85
Mf9mV0n/Xj8p/14/Kf9cPij/Ujcj/0QtGv85KBv/
WkMx/29VPf9tTzX/BwcHcwcHB0IHBwcfBwcHCgAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAHBwcEBwcHEFE1IZd5VDf/i2JD/5Jv
VP+ViX7/lYl9/6mXhf/Wzb//29DE/9nNwv/ZzcD/
2MzA/9fLv//Wyr3/1sq8/9PJvP/Uybv/08i6/9PH
uv/Sx7n/0ca5/9LHuv/Sxrj/0ca4/9HFuP/Rxbj/
0ca4/9DFuP/Qxbf/z8S3/9DFtv/QxLb/z8S3/8/D
tv/QxLf/z8S3/87Dtf/Ow7b/zsK2/87Etv/Pw7b/
zcK0/87Dtf/NwrX/zcK1/8zCtP/MwrT/zcK1/8zB
tP/MwbP/zMCz/8zBsv/MwLL/yb2w/7+zp//Fua3/
yr+x/8q+sf/Jva//ybyv/8e8rv/DuKn/vLCk/7Sp
nv+uppr/rqWY/7KonP+6r6L/v7Om/8S4qv/Dt6n/
wrao/8G2qP/Btaj/wLWn/8C1p//As6f/vrKl/76y
pP+9sKT/vLCk/7uvov+6r6L/uq2h/7quof+5raD/
ua2h/7isn/+5raD/uKuf/7ern/+3rJ//t6yf/7es
n/+3q5//uKyf/7isoP+3rKD/uKyg/7isoP+ThHb/
QDky/2ZVR/9ePyn/Xj8p/1w9KP9SNyP/RCwa/z8t
H/9lTjn/f2JK/31eQf8HBwd9BwcHRwcHByIHBwcL
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAcHBwQHBwcPUjYhl3lVOP+LY0X/
k3BV/5WJff+ViX7/qZeF/9nNwf/d0cb/3NDE/9rO
w//ZzsL/2c3B/9jLv//Wyr//1cq8/9XKvf/Uyrz/
1Mm8/9TJu//TyLv/1Mi7/9LIuv/SyLv/08e6/9PH
uv/Sx7n/0sa5/9LHuf/Rxrj/0ca4/9LGuP/Rxrj/
0sW5/9HFuP/Rxbj/0Ma4/9DFuP/Qxbj/z8W4/8/E
t//Qxbf/z8W2/8/Et//PxLf/zsO2/87Dtv/OxLb/
z8S2/87Dtf/OwrX/zcK1/83Ctf/Mv7L/wLSn/8e7
rv/Lv7L/zMCz/8u/sv/KvrH/x7uu/76xpf+zqJz/
qqCU/4+Acv+QgHL/sKaa/7uvo//AtKj/xbir/8W4
q//DuKr/w7er/8K3qf/Ctqj/wbWn/8G1p/+/s6b/
v7Km/76ypP+9saT/vLCk/7uwo/+6r6L/uq6i/7qu
ov+5rqL/ua2h/7mtoP+4rJ//uKuf/7msoP+4rJ//
uKyf/7irn/+4rKD/uayg/7isoP+5raH/uK2g/5OE
d/9AOjP/ZlZH/19AKf9fPyn/XD0o/1I2Iv9CKhr/
QC8g/2pSPP+FZk7/gmFE/wcHB38HBwdJBwcHIgcH
BwsAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAABwcHBAcHBw9SNiGXelY4/4xk
Rf+TcVb/lYl+/5WJfv+oloX/2s/C/97Ux//c0cT/
29DE/9vQxP/az8P/2c7B/9jMv//Yy77/1sq+/9XK
vf/Vyrz/1sq9/9bKvf/Vybz/1Mq8/9PJu//Vyrv/
1cm7/9TJvP/UyLv/08i6/9PIuv/TyLr/08m6/9PI
uv/TyLr/08e6/9LHuf/Sxrn/0se5/9LGuf/Sxrn/
0ca4/9HGuP/Rxrj/0Ma5/9HFuP/Qxbf/0MW4/8/F
uP/Pxbj/0MW4/9DFuP/PxLf/z8O2/8zAs//Btaj/
yb2w/83Bs//NwbT/zMCy/8m+sf/Btqn/tqqf/6if
lP+OgnT/dmJQ/56Th/+yp5v/vbKl/8O3q//Huq3/
x7ut/8W6rP/Guaz/xLis/8O3qv/Dt6r/w7Wp/8G0
qP/AtKf/wLSm/7+zpf+9s6X/vLCk/7ywpP+8r6L/
u6+i/7qvov+6rqH/ua2h/7mtof+4rKD/uKyf/7ms
oP+5rKD/uayg/7esoP+4rKD/uKyg/7mtof+4rKD/
k4R3/0A6M/9mVUf/X0Ap/19AKf9dPCj/UjYi/0Ir
Gv9CMCD/aVI9/4RnTv9+XUL7BwcHfgcHB0kHBwci
BwcHCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAHBwcEBwcHD1M2Ipd7Vjj/
jWVG/5RyV/+Vin7/lol+/6mXhf/a0MP/4NXI/9/T
yP/e08f/3dLF/9vQxf/bz8T/2c3B/9nNwP/YzcD/
18y//9bLvv/Xyr7/1sq9/9bKvf/Wyr7/1cq9/9XK
vP/Wyr3/1sq9/9XKvP/Vyrv/1cq8/9TJvP/Uybz/
1Mi7/9XIu//Vyrz/1Mm7/9TJu//TyLv/1Mi7/9PI
u//TyLr/0si6/9PIuv/Tx7r/08e5/9LGuf/Rx7n/
0ca5/9HGuf/Rxrn/0cW4/9DFt//Qxbj/zcK0/8G1
qf/MwLD/zsO1/8/Dtv/MwLL/xbut/7mvov+poZX/
eWlb/3FcSf+ViX7/qZ+T/7etoP/Ctqn/x7ut/8i8
sP/Iu67/x7uu/8a6rf/Gua3/xLms/8W4rP/Et6r/
wrap/8K2qP/BtKf/wLOm/76zpf++sqT/vLCk/7yv
o/+8sKP/uq+i/7muov+6rqL/ua2h/7mtof+4rKD/
uKyg/7isoP+4rKD/uKyg/7mtof+4rKD/ua2h/7er
oP+ThHb/Qjw0/2hWRv9fQCr/X0Ap/1w+J/9SNiL/
QSkY/0EvIf9pUj3/hGdO/31eQfoHBwd9BwcHSQcH
ByIHBwcLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAcHBwQHBwcPUzcil3tX
Of+OZkb/lXJV/5aKf/+Vin//qJaE/9zSxf/g1cr/
39XJ/9/UyP/d0sb/3tLG/9zQxP/bz8P/2s/D/9rO
wf/ZzcH/2My//9jMv//Xy7//18u//9fMv//Wy77/
18u+/9fKvv/Wyr3/1sq9/9bKvf/Wyr3/1cq9/9bK
vf/Wyr3/1cq8/9bKvf/Vyrz/1Mq8/9TJu//Vyrz/
1cq8/9TJvP/Uybz/1Mm7/9TIu//TyLv/08i6/9PI
uv/SyLr/0se6/9PHuv/Rxrn/0ca5/9LHuf/Pw7b/
w7aq/8zAsv/Pxbb/zsO2/8m9sf+8saX/rKSY/4l+
cv9pVkX/a1dJ/6GXjv+yppz/v7Sm/8e7rv/JvbH/
yr6y/8m9sP/JvbD/yLyv/8i8r//Guq3/xrmt/8a5
rP/Et6v/w7er/8K2qP/Ctan/wbWn/7+zpv+/s6X/
vbGk/7ywpP+8sKP/uq+j/7quov+6rqP/ua2h/7mt
oP+5raH/ua2h/7mtof+5raH/uKyh/7mtof+6rqH/
uKug/4+Acv9EPTb/aVdH/19AKv9fQCr/XD4n/1E2
Iv8/Khn/QzEh/2tTPf+FZ07/fF1B+gcHB30HBwdI
BwcHIgcHBwsAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAABwcHBAcHBw9TNyOX
fVc5/49mSP+VcFL/lop+/5aKfv+ploT/39PH/+PY
y//h18r/4NXI/+DVyP/e08f/3tPG/9zSxv/bz8T/
2s/D/9nOwf/ZzsL/2M3B/9jNwP/YzMH/2MzA/9jM
v//YzL//2My//9fLv//Xy7//18u+/9bLvf/Xy7//
1su+/9fKvv/Xyr3/1sq9/9bKvf/Vyr3/1cq9/9bK
vf/Vyrz/1cq8/9bKvf/Vyrz/1cq8/9XKvP/Uybz/
1Mm8/9TJvP/Uybv/1Mm8/9PIu//TyLr/0si6/9DF
t//Dtqr/zcK0/9DGuP/MwbT/wbeq/7ClnP+Ui4D/
YU08/2JOPf+SiH//qaKW/7uwpP/Guq3/zMCz/8vA
s//Lv7L/zMCy/8q+sP/KvLD/ybyv/8i8r//IvK//
xrqt/8a5rf/Fuav/w7iq/8O3qv/Ctqj/wLWn/7+0
pv+/s6X/vrKk/7yxpP+8sKT/u6+j/7uvov+6raL/
uq6i/7mtof+5raH/ua2h/7mtof+5raH/ua2g/7mt
of+4rKD/gXRk/0U9N/9oV0b/X0Aq/19AKv9cPij/
UTch/z8qGf9CMCL/bFQ9/4VoTv99XEH6BwcHfQcH
B0gHBwciBwcHCgAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcDBwcHD1M5
I5d9WDr/kGdI/5VxUv+Wi3//lop+/6mYhv/f1Mj/
5NnN/+LYzP/i18r/4dbJ/+DVyP/g1Mj/39TH/93S
x//c0cX/28/E/9vPwv/a0ML/2c7B/9rOwf/azcH/
2c3A/9rOwf/ZzcD/2c3A/9nNwf/ZzL//2c3A/9nM
v//ZzcD/2cy//9jLv//Xy7//18u+/9fMv//Xy7//
1su+/9jLv//Xyr3/1sq9/9fKvv/Wyr3/1sq+/9bK
vf/Vyr3/1cq9/9XKvf/Wyr3/1Mm8/9TJu//Vyrv/
0ca4/8S4q//Nwrb/zsO2/8W5rf+0q6D/npSI/2JQ
P/9vXUr/fG5i/6Wckf+4raH/xbms/8zAs//NwrX/
zMG0/8zBtP/MwLP/zL+y/8u/sf/KvrD/yr6w/8m8
r//IvK//x7ut/8a6rP/Fuav/xbir/8O3qf/Ctqn/
wbSn/8C0p/+/tKb/vbGl/7yxpP+7sKT/u6+i/7qv
ov+7rqL/uq6j/7qtof+5raH/ua2i/7mtov+5raH/
uq6h/7esof+AcWP/Rj02/2hVRP9gQCr/X0Aq/1w9
KP9RNSH/PycX/0QwIv9sVD3/hmhP/31cQfoHBwd8
BwcHSAcHByIHBwcKAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcHBwMHBwcO
UTchjX1YOv+QaEj/lnFS/5eLf/+Wi3//qZmH/+HV
yf/m28//5NrO/+LZzP/i18v/4dbK/+DVyP/f1Mj/
3tPI/93Sxv/d0cX/3tDF/9zQxP/c0MT/3M/C/9rO
wf/bz8H/2s/C/9rOwv/azsH/2s3B/9rOwf/azsH/
2s7B/9rOwf/ZzcD/2MzA/9jMwP/Zzb//2c3A/9nN
v//YzL//2c2//9nMwP/YzL//2Mu//9fMvv/XzL//
2Mu//9bKvf/Wyr3/1sq9/9bKvv/Vyr3/1cq8/9XK
vP/Sx7n/xLiq/83CtP/JvbH/ua6j/6SckP9lVUb/
d2NT/2RTRP+elor/saab/8K3qv/MwLP/zsO1/8/E
tv/Owrb/zcG1/8zCtP/NwbT/zMGz/8u/sv/Lv7L/
yr6x/8m9r//Jva//yLus/8e7rf/Fuaz/xbir/8S3
qv/Dt6r/wrWp/8G0p/++s6f/vbKl/72xpP+7sKT/
vLCj/7uwo/+6rqL/uq+i/7quo/+6rqL/uq6i/7qu
ov+5rqL/uayh/4BwY/9GPzj/aFVE/2BAKv9gQCr/
XD0o/1A1Iv8+Jxb/RDEh/2xUPf+GaE//fV5C+gcH
B3sHBwdHBwcHIgcHBwoAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwcHAwcH
Bw5SNiGKfVg7/5FoSP+ZclP/l4t//5eLf/+ploX/
4dbK/+Tc0P/m28//5NrN/+LZzP/g2Mz/4dbJ/+LW
yf/g1cj/39TI/97TyP/e08f/39PG/93Rxf/d0cT/
29DE/9vQwv/cz8P/28/C/9vPwv/bzsL/28/B/9rP
wv/bz8L/2s7C/9rOwf/bzsH/2s3B/9rOwf/ZzsD/
2s7B/9rOwP/ZzcD/2c3A/9jMwP/ZzcD/2c2//9jM
v//YzMD/2My//9fLvv/Wy7//1su+/9fLvv/Wyr3/
1sq9/9HHuf/Dtqn/yb2w/72ypv+on5T/cWFU/3hi
U/9nVkT/joN7/6qflv+9sqb/yb6x/8/Ft//Rxbj/
0MW4/9DFt//Ow7b/zsK2/87Ctf/NwrT/zMC0/8zA
s//Lv7L/yr6x/8q9sP/IvK//yLyu/8e7rf/Hu63/
xbmr/8S4q//Ctqj/wbWo/7+0p/++sqf/vbGl/72x
pP+8r6P/vLCk/7qvov+7r6L/uq+i/7uuo/+6r6L/
uq+i/7qvov+5rKD/gHFj/0Y/OP9nVEP/YEEq/2BA
Kv9cPSj/UDUh/z4mGP9FMiL/blU+/4ZnTv99XEH6
BwcHewcHB0YHBwchBwcHCgAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcD
BwcHDlM3IYp+WTz/kmlJ/5hzVP+Wi3//lot//6aT
gP/g18r/593R/+Xcz//l3M//5NrN/+TZzP/j2cz/
4dfK/+HWyf/h1cj/4dbI/9/Vx//f08f/39PH/97S
xf/e0sX/3dLE/93QxP/c0MT/3NDD/9zQw//b0ML/
3M/D/9vPwv/bzsL/3M/C/9vPwv/bz8H/2s/C/9rO
wf/azsH/2s3A/9rNwf/ZzsH/2c3A/9nNwP/Yzb//
2MzA/9jMwP/Zzb//2My//9jMv//YzL//2My//9fL
vv/Xy7//0cW4/7+zpv+/tKj/rKKZ/35yZv90YFD/
dmJS/3ZpXv+km5D/uK2i/8i9sP/PxLf/08e6/9LG
uf/Sxrj/0cW4/9DFuP/Qxbf/z8S3/87Ctv/OwrX/
zMK0/8zBtP/MwLL/y76x/8q+sP/Jvq//yLyv/8i8
rv/Huqv/xrqs/8S4qv/Ctqj/wbWo/8G0p//As6f/
vrGl/76wpP+8sKT/vLCj/7uuo/+7sKP/u6+i/7qu
ov+6rqL/uq6i/7mtof+AcWT/Rz43/2dSQf9hQSr/
YEEq/1w9KP9PNCH/PCUW/0UyIv9tVT7/h2hP/3hZ
PvUHBwd6BwcHRQcHByEHBwcKAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcH
BwMHBwcOUzciiX9ZPP+Takr/mXNV/5eLgP+Wi3//
pZOB/+HWy//m3tP/597R/+fc0P/j3M//5dvO/+Xa
zf/j2Mz/4tjL/+LXyv/g18n/4dTI/+DUyP/f08b/
39PG/9/Uxf/e0sX/3tLF/93RxP/d0cT/3dHD/9zQ
xP/c0MP/28/D/9vQwv/c0MP/29DC/9zPw//bz8L/
287C/9zPwv/bz8L/28/B/9rPwv/azsL/2s7B/9rO
wf/azcH/2s7B/9rOwf/ZzcD/2c3A/9nNwf/Zzb//
2cy//9bKvv/MwbX/tKme/66mm/+Kf3b/bFlJ/4Bs
Wv9jUUH/m5GI/7Gmnf/Fua3/zsO3/9PIuf/TyLr/
0si6/9LHuv/Sxrn/0sa5/9HFuf/Qxbj/0MS2/87D
tf/NwrX/zcK0/83BtP/MwLP/zL+y/8u/sf/KvrD/
yLyu/8i8rv/Hu63/xbir/8S4qv/Ctqr/wLSo/8Cz
pv/As6T/vbGk/7ywpP+8sKT/vLCk/7uvov+7r6T/
u7Cj/7qvpP+8r6T/ua6h/4BxZP9HPzn/Z1E//2FB
Kv9gQSr/XD0n/1A0If87JRf/RTIi/25WP/+GaE//
d1k99QcHB3oHBwdFBwcHIQcHBwoAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BwcHAwcHBw5TNyKJf1o8/5NrSv+bdFX/l4yA/5eL
gP+lk4H/4tjM/+jg1P/o3dT/597R/+bf0P/m3M//
5NvO/+Xazv/k2Mz/49jL/+LXyv/h18n/4dfJ/+HV
yP/g1Mj/39PH/9/Tx//e0sb/3tPG/97TxP/d0cX/
3dHE/93RxP/d0cP/3NDD/93Rw//d0MT/3NDD/9zP
w//b0ML/3NDD/9vQwv/c0MP/3M/D/9vPwv/bzsL/
2s/B/9rPwv/azsH/2s7B/9rOwf/azcH/2s7B/9rO
wf/Xy73/0ca5/8O4q/+nnJH/lYyB/2ZUQv+Db13/
aVZF/4mBdv+poZb/wLWp/83Dtv/Uybz/1Mm7/9TJ
vP/Uybr/08i7/9PIuv/Tx7r/0ce5/9HFuP/Rxbj/
z8S3/8/Dtv/Ow7X/zcK1/83CtP/MwbP/zMCy/8u+
sv/KvrD/yLyu/8i8rv/Fuqz/xbmr/8O3qv/Ctqn/
wbWo/8C0pv+/sqX/vrGl/7ywpP+8sKT/vLGk/7yw
pP+7r6P/u6+k/7qvo/+5raH/f3Jj/0dAOf9mTz3/
YUEr/2FBKv9cPif/TzQh/zslF/9GMyP/blY//4dp
UP93WT31BwcHeAcHB0UHBwchBwcHCgAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAHBwcDBwcHDlM5I4mAWz3/lWxM/5x1Vv+YjID/
l4t//6WTgv/j2s3/6uLW/+jg1P/p39P/6N7S/+Xc
0f/m3c//5tzO/+Tbzf/k2c7/5NjM/+PXy//i18r/
4tfI/+HWyf/g1cj/4NTI/9/Sxv/f08b/3tLG/97S
xf/d0cT/3tLF/93RxP/d0cX/3NDE/93RxP/d0cT/
3dHE/93Qw//c0MT/3NDD/9zQxP/c0MP/3NDD/9vQ
wv/cz8P/28/C/9vPwv/bzsL/28/B/9rPwv/azsL/
2My//9PIuv/Kv7L/s6qf/5GHgP9jUED/gm5d/3hm
VP9yZVn/opqP/7ivpP/Lv7L/0si7/9TKvP/Vyr3/
1sq9/9TJu//Uybz/1Mm7/9PIuv/SyLr/0se5/9LH
uv/Qxbn/0MW4/8/Etv/Ow7b/zcO1/83CtP/MwbP/
y7+y/8u+sf/Ku67/ybyt/8e7rf/Guqz/xbir/8K2
qv/Bt6n/wban/8C0p//AtKb/vrKl/7ywpP+9saT/
u7Ck/72wpP+8sKP/u6+i/7quoP+AcWP/R0A6/2RN
O/9hQSv/YUEq/1w9J/9PMyD/OiQX/0YzI/9vVz//
h2lQ/3dZPfQHBwd4BwcHRQcHByAHBwcKAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAcHBwMHBwcOVDojiYFcPv+VbUz/m3JP/5iM
gP+Yi4D/ppSC/+Xbz//q4tf/6d/W/+ng1f/o4NT/
6N7R/+jd0v/n3ND/5trQ/+Xbzv/l287/5NnM/+PY
zP/i18r/4tfK/+HWyf/h1cj/4NTI/+DVyP/f08f/
39LF/9/Qw//f0sX/3tLF/97Sxf/d0cT/3tLF/93R
xP/d0cX/3NDE/93Rxf/d0cT/3dHE/93Qw//c0MT/
3NDD/9vPw//b0ML/28/C/9vPw//bz8L/287C/9rN
wP/Vyr3/y8Cz/7qwpP+flYn/Y1VF/3pmVv+FcmH/
XUw9/5uTif+yqZ7/x7yv/9PHuv/Wyr3/1su//9fK
vv/Wyr3/1cq9/9XKvP/Vyrz/08m7/9PIu//Sx7r/
08e6/9HGuf/Rxrj/0cW4/8/Ft//PxLf/z8S2/83C
tP/NwrP/zMCy/8u+sf/KvrD/yLyv/8e7rf/FuKz/
xLiq/8O3qv/Dtqf/wbWn/8C0pv+/s6X/vrKl/7yw
pP+8saT/vK+j/7ywo/+8r6P/uq2h/39yY/9HQDn/
ZE07/2JCK/9hQSv/XD0n/08zIP86JBf/RjMj/29X
P/+HaU//d1k99AcHB3cHBwdEBwcHIAcHBwoAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAABwcHAwcHBw5UOiOJgVw+/5ZuTf+dc1D/
mIyA/5iMgP+nlYL/5N3Q/+rk2f/r4tf/6uLW/+jg
1P/q4NP/6d7S/+je0f/l3NH/5tvP/+bbzv/l2s7/
49rM/+TZy//j2Mv/4tfJ/+LWyv/h1cj/4NTI/+DV
yP/f1Mf/39TG/97Txf/e0sb/39LF/97Rxf/f0sX/
3tLF/97Sxf/d0cT/3tLF/93RxP/d0cX/3NDE/93R
xP/d0cP/3dHE/93Rw//c0MT/3NDE/9zQw//bz8L/
2M3A/8/Ft//Atan/pp2S/2xWRP9zYlP/fGhX/2VR
Qf+JgXf/rqaa/8G3qv/Qxbf/18u+/9jMv//Yy7//
18y+/9jLv//Wyr3/1sq9/9XKvP/Vyr3/1Mm8/9PI
u//TyLv/08i6/9LHuv/Rx7n/0cW4/9DFuP/PxLb/
z8S1/83CtP/MwbL/zL+y/8u+sf/Jva//x7uu/8e7
rv/Fuav/w7iq/8K2qf/Ctab/wLSn/7+zpv++s6X/
vbGl/7ywpP+9saT/vLCk/7uwpP+6rqH/f3Jj/0hA
Ov9jSTf/YkIr/2FBK/9cPSf/TjQg/zokF/9HMyP/
cFdA/4dpUP93WT30BwcHdwcHB0MHBwcgBwcHCgAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAHBwcDBwcHDVU5JImBXD7/l25O/511
U/+YjYD/mIyA/6aVgv/k29P/7OTa/+vk2f/p49j/
6uLW/+vh1f/q4NT/6eDS/+ff0//n3dH/5tzQ/+bb
0P/l2c7/5NrN/+TZzf/j2Mr/4tjK/+LWyv/i18n/
4tXI/+DVyP/h1Mf/4NPH/97Txv/f08f/3tPG/97S
xf/e08b/39LF/97Sxf/e0sX/3tLG/97Sxf/d0cT/
3dHE/93Rw//d0cX/3dHE/93RxP/d0cT/3dHD/9nN
wf/SyLr/xbmt/6ykmf94ZVX/k3pj/56Ebv9wX1D/
cGNY/6eflP+/tKf/zcK2/9bKvf/YzL//2czA/9nN
wP/YzL//2My//9bLv//Xyr7/18q9/9XKvf/Vyb3/
1cq8/9TJvP/Uybv/08i6/9PIuv/Sx7n/0Ma5/9DG
uP/PxLb/z8S2/83CtP/MwLP/zMCy/8q/sf/IvLD/
yLqv/8W6rP/Fuav/xLiq/8K2qP/Btaj/v7Sn/7+0
pv++sqX/vbGl/7ywpP+8sKT/vbGk/7uvof9/cmL/
R0A6/2JJNv9iQiv/YUEr/1w9J/9ONCD/NyMX/0c1
JP9wVz//h2lQ/3RWPPIHBwd3BwcHQwcHBx8HBwcK
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAcHBwMHBwcNVTkjfoJdP/+Wb07/
nnZU/5iNgf+YjIH/p5WD/+Xd0v/t5dr/7OTa/+zi
2f/q49j/6eLX/+nh1v/p4NP/6ODU/+je0v/o3tH/
5tzQ/+bcz//l287/5drO/+TYzP/j2cv/4tjL/+LX
yv/h1sn/4tXJ/+HWyP/g1Mf/4dTI/+DTxv/f08b/
39TG/9/Txv/e08b/39PG/97Sxv/e0sX/39LF/97S
xf/e0sX/3tLF/93RxP/e0sX/3dHE/93Rxf/b0ML/
1cq9/8i+sf+zqJ//hXZp/4lwWv+sk33/knli/3Ff
Tv+eloz/uK+k/8vAs//Vyr3/2M3A/9rNwf/azsH/
2c3A/9nNwf/ZzcD/2Mu//9fLv//Xy7//18q9/9XK
vf/Vyr3/1cq8/9TJvP/Uybr/1Mm7/9TIuv/Sx7n/
0MW4/9DGuP/PxLf/zcK1/8zBs//MwLP/zL+y/8q9
sf/JvLD/yLuu/8e6q//Guar/w7ep/8G1qf/Btqj/
v7Sn/76zp/++sqX/vbGl/72xpP+9saT/uq6i/4By
Yv9IQDr/Ykk2/2JCK/9iQiv/XD0n/0wzIP83JBf/
SDUj/3FYQP+Hak//cFQ67gcHB3YHBwdCBwcHHwcH
BwoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAABwcHAwcHBw1UOiR8gl5A/5dw
T/+fdlX/mI2B/5iMgf+nloP/597T/+3m3P/t5dv/
7OXZ/+zk2f/q4tj/6uLX/+nh1v/o4dX/6OHU/+ff
0//m3tL/59zQ/+fcz//m287/5trN/+TZzf/k2c3/
49fK/+LYyv/i18n/4tbJ/+DWyP/g1cj/4dPI/9/T
xv/g08f/39PG/+DTxv/f08b/3tPG/9/Tx//e08b/
3tLF/97Sxf/f0sX/3tLF/97Sxf/d0sX/3dHE/9jM
wP/MwrX/uK+k/5WKfv9+Y0//qpF7/6GHcP9vWEX/
k4mB/7Kon//IvbD/08m7/9nNwP/az8H/2s/C/9rO
wf/azcH/2c3A/9nNwP/YzMD/2cy//9fLv//XzL7/
18q+/9bKvf/Vyr3/1sq9/9XKvP/Vyrv/1Mi7/9PI
uv/Sxrn/0ca4/8/FuP/Ow7b/zsK1/87BtP/MwLL/
y76y/8m9r//IvK//x7ut/8W5rP/Et6v/w7eq/8K2
qP/Ataf/wLWn/7+ypv++s6X/vbGl/72xpP+7raL/
f3Ji/0hAOv9gRDH/Y0Ir/2JCK/9cPSj/TjMf/zkk
Fv9JNST/cVhA/4dpT/9xUzruBwcHdgcHB0IHBwcf
BwcHCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAHBwcDBwcHDVQ6JHyCXj//
mHFQ/6B3Vv+ZjYH/mI2B/6iXg//o4db/7ufd/+7m
3P/t5tv/7OTZ/+zk2P/r49j/6eHX/+rh1v/p39b/
5+DU/+bf0//o39L/593R/+fc0P/m287/5tvO/+TZ
zP/l2Mz/49jL/+LYy//h1sr/4dnJ/+DVyP/h1cj/
4NTI/+DUyP/g08f/4NTH/+DTxv/f0sb/39PG/9/T
xv/e08b/39PG/97Txv/e0sX/3tLF/97RxP/ZzsH/
0MW4/7+0qP+gl4z/cltH/6SKdP+pjXj/gGRQ/31x
Zv+poJX/xLmt/9LIu//YzcD/29DC/9vPwv/bz8L/
2s/B/9rOwf/azsH/2s3C/9rOwf/YzMD/2c2//9jM
v//Xy77/1su+/9fKvv/Wyr7/1cq+/9XKvP/Vyrv/
08i6/9PJu//Sxrn/0MW5/8/Et//Pw7b/zsG1/83B
s//MwLP/yr6w/8i9sP/IvK7/x7ut/8a5rP/Et6r/
wrao/8K2qf/AtKf/v7Om/7+zpf++sqb/v7Gl/7yv
o/9/cGL/R0A6/19DMP9jQyv/YkIr/1s9Kf9OMx//
NiMW/0g1JP9yWUH/h2lQ/3BTOe4HBwd0BwcHQgcH
Bx8HBwcKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAcHBwMHBwcNVDokfIJf
Qf+bclH/onhW/5iNgf+ZjYH/ppSB/+nf0//w6uD/
7+jf/+7l3f/t5tv/7OXa/+vj2f/r49f/6uLX/+nf
1v/o3tX/6ODU/+ff1P/m3tL/6N3R/+fcz//n3ND/
5dvO/+XZzf/k2cz/49jM/+LXzP/i18n/4dbJ/+PW
yf/h1cj/4dbI/9/Vx//g1Mf/4NTH/+DTx//g08f/
39PG/9/Sxv/f08b/39PF/97Txv/e0sX/28/D/9PJ
u//Euq3/q6OY/3RgTv+bgWr/rZR+/41zXP93Zln/
lY2D/7yxpP/Qxbj/2MzA/9vPw//c0MP/29DC/9vQ
wv/bz8L/28/C/9vPwv/azsL/2s7B/9rOwf/YzL//
2MzA/9nNv//Xy7//1su//9fLvv/Wyr3/1cq8/9XK
vP/Ty7v/1Mm7/9PJu//Sx7n/0cW4/9DEtv/Owrb/
zcK0/8zAtP/Mv7L/yr2x/8i8rv/Hu67/xbms/8S4
q//Dt6v/w7Wp/8G0p//BtKf/v7Om/7+zpf++sqb/
u6+i/39yYv9IQDr/YEQw/2NDLP9iQiv/Wz0p/04y
H/82Ixb/STUk/3NZQf+HalD/cFM57gcHB3QHBwdB
BwcHHwcHBwkAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAABwcHAwcHBw1UOiR8
hF9B/5tzUv+jeVb/mI6B/5mNgf+ikH7/5d3T/+/p
4f/v6t//7+nf/+7n3v/t5tz/7OXb/+zk2f/q4tf/
6uLW/+nh1v/p4NX/6N/U/+nf0//o39L/593R/+fd
0P/o3M//5tvN/+bbzf/k2s3/5NjL/+PYy//j18r/
49fK/+LWyf/h1cj/4dXI/+HUyP/g1cf/39TH/+DU
x//g1Mf/4NPH/+DUx//f08b/39LG/9zRxP/Xy77/
yL6x/7Kpnv9/bmD/j3Ve/66Vf/+Zf2n/bltI/5eP
hP+mnZL/yb6x/9jMv//c0MP/3dHE/93RxP/c0MT/
3NDE/9vQw//b0MP/3M/D/9vOwv/az8L/2s7B/9rN
wf/ZzcD/2MzA/9nNwP/YzL//18y+/9fKvv/Wyr3/
1cq8/9TKvP/Uyrz/1Mm7/9PIuv/Rxrj/0MW3/9DE
t//Nw7X/zsG1/8zAs//KvrL/yb2v/8i8r//Hu63/
xbms/8S3q//Dt6n/wrao/8C1p//AtKf/v7Sm/7+z
pf+8r6L/fnFh/0dAOv9bPSn/ZEMs/2JCK/9cPSf/
TTIf/zYjF/9JNiX/cllB/4prUP9wUznuBwcHdAcH
B0EHBwcfBwcHCQAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcDBwcHDVY6
JXuFX0L/nHRT/6N7Wf+ZjYH/mY6B/6GPfv/n3dT/
8Ori/+/p4f/v6d//7une/+7o3v/u593/7eXa/+zk
2f/r49n/6uLX/+vh1f/p4NX/6N/U/+ff0//m39L/
597R/+fd0P/m28//5dvO/+bazv/l2sz/5dnM/+PZ
zP/j1sn/49fJ/+PWyf/h1sn/4tTI/+DUx//g1Mj/
4NTH/+DVx//f1Mf/4NPH/+DUx//f0sb/2M3A/8zC
tf+3raT/kIN0/4RqVP+sk33/o4dz/3VeSv+QiH7/
qqKW/7Wqn//Sx7v/3NDD/97Sxf/e0sT/3NDE/93R
xP/c0MP/3NDE/9zPw//c0MP/3NDD/9vPwv/bz8H/
2s7C/9rOwf/ZzcD/2c3A/9nNv//ZzL//2Mu//9jL
v//Wyr3/1cq8/9XKvP/Ty7v/08i7/9PHuv/Sxrn/
0MW4/8/Et//OwrX/zMGz/8zAs//Lvq//ybyv/8i8
r//Fuqz/xbmr/8O3qv/Ctqr/wrWp/8G1p/+/tKb/
vrOn/7yvo/9+cWH/R0A5/1w9KP9kQyz/Y0Ir/1w9
J/9MMiD/NSIW/0o2Jf9zWUH/iGpQ/3BTOe4HBwdz
BwcHQQcHBx8HBwcJAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcHBwIHBwcN
Vzole4ZgQv+edVX/pXxZ/5mNgf+ZjYH/opB+/+fe
1v/x7OT/8evj/+/q4f/u6eD/7uje/+7o3f/u593/
7ubc/+3l2v/r49j/6uLX/+rh1v/r4NX/6eDT/+nf
0//n3tP/5t7S/+bc0P/m3ND/5tzP/+Xbzv/l2c3/
5tnM/+TZy//j2Mv/49jK/+PWx//i18j/4tXI/+HU
yP/h1Mj/4NTH/+DUyP/g1Mf/3tPG/9vPwv/Qxrn/
vrSn/56TiP94Xkr/p413/6qQef+FaVX/hHhr/6qi
l/+7sKT/v7Oo/9fLvv/e0sX/3tLF/97Sxf/e0sX/
3dHF/93RxP/d0sT/3dHD/9zQw//c0MP/29DC/9zP
w//bzsL/2s/C/9rOwf/azsH/2c3A/9jMwP/YzL//
18u//9jLv//Xyr3/1cq8/9XKvP/Vyrv/08i6/9LH
uf/Qxrn/0MW3/87Etv/NwrX/zMCz/8y/sv/KvrD/
yLyv/8e7rf/Fuqz/xLiq/8K2qv/Ctqr/wbWo/7+0
p/+/s6b/vK+j/35xYf9HQDr/XD0o/2RDLP9jQyv/
XD0n/00yH/81Ihb/SzYl/3NZQv+IalD/bVE36gcH
B3MHBwdBBwcHHgcHBwkAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwcHAgcH
Bw1XOyZ7hmJE/592Vv+nflr/mY6B/5mNgf+ikH//
6N/X//Lt5f/y7OT/8ezj//Hq4f/u6eD/7ujd/+7n
3P/u5tv/7ubc/+3m2v/s5Nn/6uPX/+rh1v/p4dX/
6ODV/+rg0//n39P/6N3S/+fc0f/m3ND/5dvP/+ba
zv/l283/5NnM/+TZzP/k2Mv/49fJ/+PXyv/i1sj/
4tXI/+LWyP/h1cj/4NTI/9/Uxv/d0cT/1Mm8/8O5
rP+ooJT/b1pH/56Ebv+ulX7/kXdg/3VjVf+jm5H/
vbKm/8a6r//Guqz/2s/C/97Sxf/f0sX/3tLF/97S
xv/e0sX/3dHE/93Rxf/d0cX/3dHE/9zQxP/c0MT/
3NDD/9zQw//bz8L/28/C/9nOwf/azcH/2c3A/9jM
wP/YzL//18u//9fKvv/Wyr3/1cq+/9TJvP/Uybv/
0si6/9HHuf/Qxbf/z8S3/87Ctf/NwbT/y7+y/8u/
sf/JvbD/yLus/8a6rf/Fuqz/xbir/8O3qf/Ctqj/
wLWn/8C0pv+8sKT/fm9h/0k/Of9bPin/ZEMs/2ND
K/9cPSf/SzEf/zUiFv9LNyX/dFpC/4lrT/9rTzbp
BwcHcgcHB0AHBwceBwcHCQAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcC
BwcHDVc7JnuIYkT/n3dV/6d/W/+ZjoH/mY2B/6OQ
gP/o4dj/8+3n//Lt5v/x7OT/8ezj//Dr4v/v6uH/
7uje/+7n3f/u5tv/7eXb/+zl2f/t5dr/7OTY/+vj
1//r4dX/6uDU/+nf0//o39L/6N3R/+fd0f/m3ND/
5tvQ/+Tazv/k2s3/5dnM/+PZy//k2Mv/49jK/+PX
yv/i1sj/4tbI/+HVyP/h1cj/3tPF/9XKvv/JvbH/
sKid/3tpWf+TemP/r5Z//5yCa/9uWEX/m5OI/7es
o//LwLP/zcG0/8m+sf/b0MT/39PH/97Txv/e0sb/
39LF/9/Sxf/e0sb/3dHE/93RxP/c0MT/3dHE/93Q
w//d0cT/3NDD/9vQw//bzsL/2s/B/9rOwv/azcH/
2c3A/9nNwP/Zzb//2Mu+/9fLvv/Wyr3/1sq9/9XK
vP/TyLv/08e5/9HFuP/PxLf/zsO2/83Ctf/MwrP/
zMCy/8q+sf/Iva//x7ut/8a6rP/FuKv/w7eq/8O3
qv/Btaj/wbWn/7ywo/9+cGD/SUA5/1w+Kv9kRCz/
Y0Ms/1s9J/9LMR//NCIW/0s3Jv90WUD/iGpQ/2pO
NukHBwdyBwcHQAcHBx4HBwcJAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcH
BwIHBwcNVjolc4hjRf+feFf/qYBd/5qOgv+ZjoL/
o5GA/+nj2f/z7uj/8+7n//Lt5v/x7eX/8ezk//Dr
4v/v6eH/7+nf/+7o3v/t5tz/7OXb/+zk2v/s49j/
6+TY/+vh2P/s4db/6uDU/+nf0//n39P/6N3S/+fd
0f/m3ND/5tzQ/+bbz//l2s7/49rN/+PZy//j2Mr/
49nL/+LXyf/i1sn/49fJ/9/Uxv/ZzcH/zMK1/7at
ov+IfG7/iG9Z/66Ufv+liXT/e2FN/42Dd/+vppv/
yb6x/9XKvf/Rxbj/y7+y/93Qxf/f08f/4NPG/9/T
xv/e08b/3tLG/9/Sxf/f0sX/3tLF/97Sxf/d0cX/
3dHF/93RxP/c0MT/28/D/9vQwv/bz8L/287C/9rO
wf/bzsH/2s7A/9nNwP/Zzb//2Mu+/9fLvv/Wy77/
1cq8/9TJu//TyLr/0ca5/9HFuP/PxLb/zsS2/8zC
s//Lv7L/zMCy/8q+sP/IvK//x7ut/8W5rP/EuKz/
xLiq/8O3qf/Btaj/vq+i/31wYP9JQDn/XD4q/2RE
LP9kQyz/Wz0n/0syH/80Ihb/TDYk/3RaQv+Ka1D/
a0436AcHB3EHBwdABwcHHgcHBwkAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BwcHAgcHBw1UOiRuiGNF/6F5WP+qgmD/mo6C/5mO
gv+ikYD/6ePZ//Xw6f/07uj/8+7n//Pt5f/y7eT/
8evk//Dr4v/v6uH/7+nf/+7o4P/u59z/7ebb/+zk
2v/r49n/6+HY/+zj1v/q4tf/6uHW/+ng1f/p39P/
6N3S/+fc0P/n3ND/59vP/+Xbzv/l2s7/5NnN/+TZ
zf/i2Mr/49jK/+LYyv/i1sn/29DD/9DFuf+9sqb/
l4yB/31iTv+qkXv/q5F7/4pxWv9/b2L/qKCV/8O4
rP/Uybz/2s7B/9LHuv/Lv7L/3tHG/+HVyP/h1Mj/
4NTH/+DTx//f08b/39PG/97Txv/e0cX/3tLF/97S
xf/d0cT/3NDE/93RxP/d0cP/3NDD/9zQw//bz8L/
287B/9vPwv/bzsH/2s7A/9nNwP/YzL7/18y+/9fK
vv/Wyr3/1cq8/9TJu//TyLn/0ce4/9DFt//PxLb/
zsK1/8zBtP/MwLL/yr6x/8i8sP/Huq7/x7ut/8a5
rP/FuKv/w7ep/8K2qP+9sKT/fnBg/0tCOv9dPyn/
ZEQs/2RDLP9cOyf/SzEf/zQiFv9MNyb/dVpB/4hq
UP9rTjfoBwcHcAcHBz8HBwceBwcHCQAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAHBwcCBwcHDVU5JW6IZEX/oXxa/6yCYP+aj4L/
mo+B/6ORgf/q5Nr/9fDq//Tv6f/07+j/8+7n//Lt
5v/x7eX/8ezj//Dr4//v6uH/7+nf/+7o3v/u6N3/
7ubc/+3m2//s5Nn/6+HY/+ri1//q4db/6eHV/+rg
1P/o4NT/6N7S/+jd0f/n3ND/5tzP/+Xbzv/m2s3/
5NrN/+TZzP/j2Mv/4tfK/97Sxv/Uyr3/w7mt/6Oa
j/9yW0j/o4dy/6+Wf/+WfWX/cV9O/6Kaj/+8sqb/
0Ma5/9rNwf/d0sT/0sa6/8vAsv/e0sb/4NbI/+HW
yP/h1cj/4dTI/+DTx//f1cf/39PH/97Sxf/f0sX/
39LF/97Sxf/e0sX/3dHF/93RxP/c0MP/3NDD/9vQ
wv/cz8P/3M/C/9rPwv/azsD/2c7A/9nNwP/Zzb//
18y//9fLvv/Vyr3/1Mq8/9PJu//TyLn/0sa4/8/F
t//Ow7X/zcK1/8zAs//Mv7L/yr2w/8i8rv/Gu63/
xrms/8W5q//DuKr/wraq/72wo/98bl7/TUQ8/19A
Kf9kRC3/ZEMs/1w7J/9MMR7/MyIW/004J/92WkL/
i2xQ/2tON+gHBwdwBwcHPgcHBx0HBwcIAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAcHBwIHBwcNVTslbohlSP+je1r/rIRi/5uQ
gv+ajoL/o5KB/+rl3P/28ev/9fDq//Tv6f/07uj/
8+7n//Pt5v/y7eX/8ezk//Hr4f/w6uD/7unh/+7p
3v/u597/7ubc/+3l2//s5dr/6+PY/+ri1//p4dX/
6uDU/+vh0//p39P/6d/S/+ne0v/n3ND/5tvP/+bb
zv/l2s3/5drN/+TYzP/g1cj/2MzB/8m+s/+uppv/
dmJR/5mAaP+xmIH/oIRv/3FbRv+WjYL/taui/8zC
tf/ZzcD/39PG/97Sxv/Sx7n/y7+y/97Txv/h18n/
4dbI/+DWyP/h1cj/4dXI/+DUyP/g08f/3tTG/97T
x//e0sb/39LG/97Sxf/d0cT/3dHE/93RxP/d0cP/
3NDE/9zQw//cz8P/28/C/9rPwv/azsD/2c7A/9jM
wP/YzMD/18u//9bKvP/Vyr3/1Mq8/9TJu//Rx7j/
0MW4/8/Etv/NwrX/zcG0/8zAsv/KvrH/yb2v/8e7
rv/Hu67/xbms/8S3q//Dt6r/vLCi/2NYS/9PRj7/
YEEq/2VELf9kQyz/XD0n/0oxHv8zIhb/TTkn/3Vb
Q/+Ka1D/a0835wcHB28HBwc9BwcHHQcHBwgAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAABwcHAgcHBw1WPCZuiWZI/6R9XP+th2T/
nJCC/5qPgv+jk4H/6+be//fy7P/28ez/9vHr//Xw
6f/07uj/8+3n//Pt5v/y7OX/8uzk//Hr4//w6uL/
7+nf/+7o3v/u6N3/7ufc/+3m2//t5dr/6+TZ/+vj
2P/q4db/6ODV/+jg1P/o39L/6d/S/+ne0v/o3tH/
593Q/+Xazv/l2s3/4tfK/9vRxP/Ow7f/tq6j/4Jy
ZP+OdV3/sJd//6iLdv+EaFP/h3xw/62mm//HvLD/
1sq+/97Sxf/h1cj/39LG/9LIuf/Lv7L/39PI/+LW
yv/i18n/4dnJ/+HWyP/h1cj/4dTI/+DUx//g1Mf/
4NTH/9/TyP/f08f/39LF/9/Sxf/e0sX/3dHE/9zQ
xP/d0cP/3NDE/9zPw//b0ML/28/C/9rPwv/azsH/
2c3A/9jNwP/Xy7//1su+/9bLvf/Vyrz/1cq7/9LI
uv/Rx7n/z8S2/87Dtv/NwrX/zMGz/8u/sv/KvbD/
ybyv/8e7rv/Huq3/xbmr/8S4qv+9rqH/YldK/1BG
Pv9gQSr/ZUUt/2RELP9bPSf/SjEe/zMiFv9NNyX/
dlpC/4psUP9lSzTjBwcHbwcHBz0HBwccBwcHCAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAHBwcCBwcHDVY8Jm6LZ0j/pX5d/6+J
Zf+ckIL/mo6D/6ORgf/s5t//+PPs//fy7P/28ev/
9fDr//Xv6v/07+n/8+7o//Lt6P/y7eb/8ezl//Dr
4//w6uL/7+ni/+/o3//u5+D/7uXd/+3l2//t5dr/
7OTZ/+vj2P/q49f/6uHW/+nf0//p3tP/5t7S/+je
0f/o3dH/593Q/+bazv/e1Mj/0si8/7uzqP+ShXr/
hGhT/62Ufv+sk3v/kHZe/3lnWv+lnZP/wrer/9PI
u//d0cT/4NTH/+LVyP/f08X/0ca6/8vAs//g1cj/
49fL/+PXy//j18n/4tfJ/+LXyf/h1sj/4NXI/+HU
yP/h1Mj/4dTH/97Tx//e08b/3tLG/97Rxf/e08b/
3tLF/93Rxf/d0cT/3dHD/9vPw//b0ML/28/C/9rP
wv/azsH/2c3A/9nNwP/Xy77/18q9/9XKvP/Vyrz/
08i7/9LHuf/Rxbf/z8S3/87Dtf/NwrT/zMG0/8u/
sf/JvrD/yLyv/8e7rv/Guq3/xLir/7ywo/9iV0r/
UEY+/2FBK/9lRS3/ZEQs/1s9J/9KMB7/MyEW/005
J/92W0L/imxQ/2RLNOIHBwdtBwcHPQcHBxwHBwcI
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAcHBwIHBwcNWDsmbYtoSv+ngF//
sIhn/5yQgv+ckIP/no2A/+rm3v/49O3/9/Pt//fy
7f/28ez/9vDs//Xw6v/08On/8+/o//Lu5//y7eb/
8e3l//Ds5P/v6+L/7+ri/+/p4f/u5+D/7ufe/+7m
3P/t5dv/7OTa/+vj2P/q4tf/6uHW/+ng1f/p39P/
6N7R/+jd0f/l28//4tjK/9fNwf/Cuq//o5mN/3lf
S/+ulX3/spmB/5yAav9vWkf/npeM/7qxpv/Qxbj/
29DD/+DUx//h1cj/4dbI/9/Txv/Qxbj/zMGz/+HV
yf/j2Mv/5NnL/+PYzP/k18v/4tbJ/+LXyf/g1sj/
4dTI/+LVyP/g1Mj/4NTH/9/Ux//f1Mf/3tLF/9/T
xf/e0sX/3dHE/93Rw//d0cT/3dDD/9zQxP/b0ML/
28/C/9rPwv/azsH/2c3A/9nMv//Xy77/18u+/9XK
vP/Uybz/08i6/9HGuP/Qxbj/z8S2/87Dtf/NwbT/
zMCy/8u+sv/Jva//x7uu/8e7rv/Fuaz/vbCj/2JW
Sv9QRj7/YEEq/2dFLf9kRCz/XD0n/0owHv8zIhb/
Tjgm/3dbQ/+Ia1D/ZEoz4gcHB20HBwc9BwcHHAcH
BwgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAABwcHAgcHBwxYOydtjGlK/6iB
YP+xjGr/nZGD/5yQhP+ci33/6uXd//f17//48+7/
+PPu//fz7f/38uz/9PHs//Xx6v/18Or/9O/p//Tu
6P/y7ef/8u3l//Ht5P/w7OP/7+vi/+/q3//u6d7/
7ujd/+7n3f/s5dv/7OTa/+vk2P/q4tf/6uHW/+nh
1f/q4NT/6N7S/+Xazv/ZzsX/ysC0/62lmv9yXEn/
pYt0/7mgiv+liXH/el9L/5KIf/+zq6D/y8G1/9rN
wf/g1cb/4dXI/+HVyP/h1cj/4NPG/9HGuP/MwLP/
4dbJ/+XazP/k2s3/49jL/+TYyv/i18v/49bK/+LW
yv/i2Mn/4tbI/+HWyP/h1Mj/4dTI/+HUx//f1Mf/
3tPG/9/Txf/e0sX/3tLF/93RxP/d0cX/3NDD/9zQ
w//b0ML/28/C/9rPwv/azcH/2c3A/9jMv//XzL7/
18q+/9bKvf/Uybv/0si5/9HGuP/Qxbf/z8S2/83C
tf/MwbT/zMCy/8q+sP/IvbD/yLyv/8e7rf+9sKP/
YlZJ/1FHPv9hQSr/Z0Ut/2RELf9cPSf/STAd/zIh
Fv9OOCb/d1tD/4hrUP9lSTThBwcHbQcHBz0HBwcc
BwcHCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAHBwcCBwcHDFk8J22Oakv/
qoJi/7OMa/+dkoP/nJCD/5yMff/r5d3/+PTx//j1
8P/39e//+PTt//fz7P/38+z/9vLr//bx6v/18On/
9e/p//Tu6P/07eb/8u3l//Hs5P/x6+P/8Org//Dp
4P/u6eD/7ufd/+3n3f/s5tv/7Oba/+vj2f/q4tj/
6uDX/+ng1f/m3dL/3dXJ/83Gu/+1rKT/fWlZ/5qA
aP+6oov/rJJ6/4pwWf+Ddmn/rKab/8a7sP/Wy7//
39TG/+LVyP/i1sj/4dXI/+HVyP/f1Mf/0MW4/8zA
s//i2Mr/5trN/+Xazf/l2cz/5drM/+TZy//k2cr/
4tjL/+LXyf/i18r/4dnJ/+LXyf/i1sn/4dXI/+DU
x//g1cf/3tPH/97Tx//e0sX/39LF/93RxP/d0cT/
3NDD/9zQw//b0ML/28/C/9nOwf/ZzsH/2MzB/9jM
v//Wy77/1sq+/9XKvP/Uybr/08i6/9HHuP/PxLf/
zsO2/83Ctf/MwbP/y7+y/8q+sf/IvK7/x7yu/72x
o/9iVkn/UUc+/2JCK/9nRi3/ZUQt/1w7J/9JMB7/
MSIX/085Jv93W0P/iWtR/2VJNOEHBwdsBwcHPAcH
BxwHBwcIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAcHBwIHBwcMWDsoZ45q
TP+pgmL/tY5u/56Rgv+ckYT/nY1+/+vl3//59fL/
+Pfx//j28P/59e//+fTu//fz7f/38+z/9/Hr//Xw
6//18Or/9e/p//Tu5//z7eb/8u3l//Ls5P/x6+P/
8Ovi//Dq4P/v6d//7+jd/+7l3f/t5tv/7OXa/+zk
2v/r49n/6d/W/+DZzf/TycH/vbas/4x/cv+OdFz/
uaCJ/7OXf/+XfWX/dWJS/6Sdk//Ct6v/0sq+/9/T
x//j1sn/4tfJ/+HWyP/i1sj/4dXI/9/Uxv/Rxrj/
zcK1/+LYy//l287/5tzO/+Xazv/m2s3/5dnL/+TZ
zf/k2Mv/49jL/+PXzP/i18n/4tfK/+HWyf/h18j/
4tbI/+HVyP/g1Mf/39TH/97Txv/e0cX/3tPG/97R
xP/c0MT/3dHE/9zQw//b0ML/287C/9rOwv/azsH/
2MzA/9fLv//Xy77/1cq8/9TKu//Uybv/0se5/9HG
uP/Qxbf/zsS2/8zBtP/LwLL/zMCy/8q+sP/IvK//
vbGk/2JWSf9QRj3/YkIr/2ZGLv9lRS3/XT0n/0kw
Hv8yIRb/Tzkn/3ZbQv+LbFD/Zkk04AcHB2gHBwc6
BwcHGwcHBwcAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAFE3IDdNMByLVDYecVU5JGtbPimC
jmtN/6uGZP+2j27/nZKD/5yRhP+djX7/6+fg//r4
8//5+PH/+ffx//r28P/69e//+fTv//jz7v/38+3/
9vHs//bx7P/18Ov/9e/p//Tu6P/z7uf/8u3m//Lt
5f/x6+T/8erj//Dq4P/v6d//7ujd/+7n3f/u5tv/
7eXb/+zj2P/l29L/2M/H/8O8sv+ckYb/g2dR/7Wb
hP+5n4X/pIZu/3FbR/+blIr/urCn/9DGuv/d0sf/
49jK/+TZy//j2Mr/49fJ/+HWyP/i1cj/39PG/8/E
uP/NwrX/49nN/+bc0P/m3M//5tvP/+bczv/l287/
5trN/+Xazf/j2Mv/5NnL/+PYzP/j18r/4tfK/+LX
yP/h1sj/4tXJ/+HVyP/h1cj/4NXH/9/Txv/f08b/
39PG/97Sxf/c0MT/3dHE/9zQw//c0MP/287C/9nO
wf/ZzcH/2M2//9fLvv/Wyr3/1cq8/9TKvP/Uybv/
0se5/9HFuP/QxLb/zcK1/8zAtP/Lv7L/yb6w/8q9
sP+9saT/YlVI/1FHPv9iQiv/aEYu/2VFLf9cPSf/
TDIe/zIiFv9POSf/d1xC/4hqUP9kSjPaBwcHXgcH
BzMHBwcYBwcHBwAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAUTQgXGI/J956VTntgl5B7XdY
PO+Pa03/rYZm/7iTcv+dkoT/npKF/56QgP/s6OD/
+vnz//r48//79/H/+/fx//n28f/69fD/+fTv//jz
7v/48+3/9/Ls//bx7P/28ev/9fDq//Tv6P/07uj/
8u3n//Ls5f/x7OT/8Ovj//Dq4v/v6d//7uje/+7n
3P/t5dr/6OHW/93Vy//Kw7n/qaSb/3lfS/+tk3z/
vqSM/6uOdv+GaVT/jIN4/7Osov/LxLj/3NHG/+LX
yv/k2Mz/49jL/+TXyv/k2Mr/49fK/+PXyf/f08b/
z8S3/83Ctv/j2c3/593Q/+fc0f/n3ND/5tvP/+bb
z//l3M//5tvO/+XazP/l2s3/5NnM/+PYy//k2Mv/
4tfK/+LXyv/i18n/4tbI/+DVyP/g1cj/39TH/9/V
yP/f08f/39PG/9/Txv/d0cX/3dLE/93QxP/cz8P/
28/C/9rOwf/ZzcD/2c3A/9bLvv/Wyr3/1cq8/9TJ
vP/Tx7r/0sa5/9DFt//PxLb/zcK1/8zBs//Lv7L/
yr2x/7+yo/9iVUj/UUY9/2NDK/9oRi7/Z0Ut/1w9
KP9NMR/+MSIX/003Jf9yVz7/hGZK/2FEL84HBwdO
BwcHKQcHBxMHBwcFAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAABSNh5dbEgv6otlR/+adVf/
jGlK/49sT/+rh2j/uZVz/5+Thf+ekoX/n5GA/+3p
4v/7+vX/+/n0//v58//79vP/+fXy//n28f/49vD/
+fXv//j07v/39O3/9/Ps//by7P/28ez/9fHq//Tw
6f/z7uf/8+7m//Lt5f/x7eT/8evj//Dq4v/v6eH/
7ufe/+vk2v/i29H/z8nB/7avqP95YlD/pYhw/8On
kv+xlX//lXlg/31sXv+rpp3/xr+z/9jPxP/k2cz/
5drO/+Xazv/k2cz/5NjM/+PYy//k18j/49fK/+DU
yP/PxLj/zsS3/+Tazv/o3tL/597R/+fd0f/l3NH/
5dzR/+bcz//m3M//5dvP/+bazf/l2s3/5NnM/+Ta
zP/j2Mz/49jK/+LXyv/h18n/4dbJ/+HXyf/g1cj/
4dXI/9/UyP/f08f/39PG/97Txf/e0sX/3dLE/93Q
xf/cz8P/2s/B/9rOwf/ZzcD/2My//9fMvv/Wyr3/
1cq9/9PIu//Sx7r/0ce5/8/Ftv/PxLb/zcK1/8zA
s//Mv7L/v7Kj/2JVSP9RRz7/Y0Ms/2lHLv9nRS3/
XT0n/00xH/4sHBT/Qy4g/2JHM/9vUzn/Y0UuwwcH
BzcHBwccBwcHDQcHBwMAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAFI2Hl1tSS/qj2hJ/554
Wv+ObE3/kW1Q/62Jaf+5lXX/n5OF/5+Thv+gkoD/
7urj//z79v/8+PX/+/n1//v59P/69vP/+fjy//n3
8f/59vH/+PXw//n17//48+7/9/Pt//fy7P/28ez/
9fHr//Tw6v/z7uj/8+3n//Lt5v/y7OT/8Ozj//Dr
4v/t593/5d7V/9TOx/+9t7D/hHNl/5p9Zf/Bp5H/
vqSM/6KFbP9zXUr/pJ2W/8C5r//VzMH/4NjM/+fd
0P/n29D/5tvP/+Xazv/l2s3/5NnL/+PXy//i18r/
39XI/8/FuP/NxLn/5tvQ/+ff0//o3tL/6N3S/+nd
0f/n3dD/593R/+bcz//m28//5tzP/+Xbz//m283/
5drO/+TZy//j2Mz/49fL/+PYzP/j2cr/4dfJ/+LW
yf/i1cn/4dTI/9/UyP/e1Mf/39PH/97Sxf/d0sX/
3dLF/93QxP/c0MP/2s/B/9rOwv/ZzcD/2c2//9fM
v//Wyr3/1cq9/9TJuv/SyLr/0Ma4/8/Et//Ow7X/
zMK0/8zAs//AsaP/YlVG/1JHPv9jQyz/aUcu/2ZG
Lv9dPif/TjIf/BwUDtcpGhLOMCIXpkMxIJdJNSRr
BwcHIQcHBw8HBwcHBwcHAQAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAVDYeXW1JL+qPaEn/
nnla/45sTf+Sb1L/ropq/7qWd/+flIb/n5OH/6GU
g//t6+X//Pv3//z69v/8+vb//Pj1//v59P/6+fT/
+vjz//n38v/59vH/+vXw//n07//49O7/+PPt//fy
7P/28ez/9vHr//Xv6v/17un/9O7n//Pt5//y7OX/
7+ri/+nj2f/b1c7/xL+3/5WJf/+OcVn/vKKK/8Wo
kf+tj3f/gGRO/5iQhv+6san/0Mq+/+HXy//n3dD/
6N7S/+je0f/m3dD/5tzP/+bcz//l2s3/5dnN/+TZ
zP/g1cj/z8W3/8/FuP/l29L/6uDU/+rg1P/n39P/
6N7S/+je0f/o3dH/5t3S/+Xd0f/k3ND/5tzP/+Xc
zv/m287/5drN/+TZzP/l2sz/5NnM/+PYy//j2cv/
4tfK/+LWyv/i1sr/4dTI/+HVyP/g1Mf/39PH/97T
xv/e0sb/3tLF/9zQw//c0MP/2s/B/9rNwf/ZzcD/
2My//9bLv//Vyr3/1cq8/9TJu//Sx7r/0ca4/8/E
t//NxLb/zMK0/8GypP9hVEf/U0g9/2RDLP9qRy//
aEYu/109J/9OMh/5BwcHlAcHB3gHBwdYBwcHPAcH
ByQHBwcSBwcHBgcHBwMHBwcBAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAABSNh5dbUkv6o9o
Sf+eelr/jmtN/5NwUv+wi2z/vJl5/6CVh/+glIf/
o5OE/+7s5v/9/Pf//fv3//z79v/8+vb/+/r2//v6
9f/7+fT/+vjz//r38v/69/L/+fbx//n08f/59e//
9/Tv//fz7f/38+z/9PLs//Xw6//07+n/8+7o//Lt
5v/t5+D/4NvT/8vGv/+mnZX/hGZS/7aZgf/HrZb/
tph//5B0W/+Ge2//s6yl/8vFu//e1sr/5d7R/+rg
1P/q3tP/6d7S/+je0f/o3dD/59zP/+bcz//l2s7/
5NrN/+HWyf/Qxbj/0MW5/+Xd0v/q4NT/6eDV/+ng
1f/q4NT/59/T/+fe0//o3tH/593R/+bd0v/l3dH/
59zQ/+fd0P/m287/5tvN/+Xbzv/l2sz/49nM/+TZ
zP/j18v/49jK/+LXyv/i1sn/4dbI/+DWyP/g1Mf/
4NTH/97Uxv/e1Mb/3tLF/9vQxP/c0MP/28/C/9vO
wf/ZzcD/2My//9bMv//Vyr3/1Mq7/9TJu//Sx7n/
0ca4/9DFt//Pw7b/wbWk/2BTRv9VST7/ZEMs/2pI
L/9mRS7/XT0n/00yHvkHBweOBwcHbwcHB0wHBwcu
BwcHGQcHBwgHBwcBAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAFI2Hl1tSS/q
j2hJ/556Wv+PbE3/lHFT/7GNbf+9mnn/oZWH/6CU
iP+jloX/8Ozm//38+P/9/Pj//fr4//z79//8+/f/
+/r2//v69f/7+fX/+vf1//r48//69vP/+ffy//r2
8P/39e//+PTu//j07v/38+z/9vHs//Xw6//07+n/
7uzj/+Xg2f/SzMb/tK+o/3pfTP+ukXn/yq6Y/72f
hf+hg2r/emZV/6umnv/Hwbn/29TJ/+bc0//r4NX/
6eHV/+rf1P/p39P/6d7S/+je0f/n3dD/59zP/+bc
zv/m287/49fK/9DFuP/Rx7r/59/U/+nh1//p4NX/
6eDV/+rh1v/p4NX/6d/T/+fe0//n3tP/6N/R/+jd
0v/n3dH/5t3Q/+fd0P/n28//593P/+bbzv/m2s3/
5NnM/+TXzP/j2Mv/49jK/+LYyf/i2Mr/4tfJ/+DV
yP/g1Mj/4NTH/97Ux//f08b/3tLF/9zRxP/c0cT/
28/B/9vNwf/YzMD/2My//9bLvv/Vyrz/1Mm8/9PI
u//Sx7n/0Ma5/9DFtv/BtKT/YFNG/1RJPv9kRC3/
a0gv/2hGLv9dPSf/TTAe9QcHB4wHBwdtBwcHSAcH
ByoHBwcUBwcHBgAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUjYeXW1J
L+qPaEn/nnpa/49sTf+UcVT/so1u/76aev+ilob/
oZaI/6GTg//u6+b//v35//79+f/++vj//fz4//z8
+P/8+/f//Pv3//z69v/7+vX/+/n1//r49P/59/P/
+fXy//j28f/49fD/9/Tv//j07v/38u3/9vHs//Lt
6P/p5d7/2NPN/766tP+Aalv/podu/8etlf/Dp43/
rY91/3pfS/+jnZf/wry0/9fQyf/m3tP/6uPX/+rj
2P/q4tf/6eHW/+ng1f/o39T/597T/+ne0f/o3dD/
59zQ/+fbzv/j2Mr/0MW4/9LIvP/o4NX/6+PZ/+ri
1//p4df/6eHV/+ni1f/r4dX/6uDU/+nf0//p39P/
6d7T/+jf0v/m3tL/593R/+bd0P/m3dD/59vP/+Xb
z//l2c3/5dvN/+XZzP/j2cz/49nM/+LYyv/j18r/
4tfJ/+HWyP/g1Mn/4NTI/+DUyP/e08f/3tPG/9zR
xP/bz8P/28/B/9vNwf/ZzcD/2My//9bLvv/Vyr3/
1Mm8/9TJu//Sxrn/0cW4/8K1pf9fUkX/VUk+/2RF
Lf9sSTD/aUYu/109J/9MMR30BwcHiwcHB2wHBwdH
BwcHKgcHBxQHBwcGAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABUNh5d
bUkv6o9oSf+eeVr/kW5P/5RxVP+yjm7/wJt8/6OX
if+jl4r/npGA/+3r5f/+/fr//v36//79+f/++/n/
/fz5//z8+P/9/Pj//Pv3//z69v/7+vb/+/j2//v3
9f/6+PP/+ffz//n38v/69vD/+PXw//f07//28ez/
7urk/9/b1f/Ewbz/jX9z/5t9Y//Ep5D/yKyT/7aY
fv+Lblb/kYiA/7u1rv/Tzcb/49zS/+vj2f/s5dv/
6+TZ/+vk1//r4tf/6eLV/+nh1f/o39T/597T/+fe
0//n3dH/59zQ/+PYy//Qxrn/08i9/+jh1v/s5dr/
7OLa/+vj2f/q4tf/6uDX/+nh1v/r4dX/6+HV/+ng
1f/o39T/6d7T/+nf0//o39L/5t7S/+jd0P/n3tH/
5tzQ/+fczv/m28//5tvN/+TZzf/k2cz/49nM/+PY
y//j18v/4tfK/+HXyP/g1cn/4NbJ/+DUyP/e1Mb/
3tPH/9zQxf/c0MT/28/D/9vOwv/ZzcD/2MzA/9bM
vv/Vyr3/1Mm8/9PIuv/Sx7n/w7am/19SRf9VSD7/
ZkUu/2xJMP9pRy7/XT0n/0wxHvMHBweLBwcHawcH
B0YHBwcpBwcHEwcHBwYAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFI2
Hl1tSS/qj2hJ/555Wv+Tb1D/lHBU/7KPb//AnX3/
pZaI/6OYiv+fj3//7evl//7+/P/+/fr//v36//79
+v/+/fr//fz5//38+f/9/Pj//fr4//z79//8+vb/
+/r2//v59f/6+PT/+vbz//n48v/59/L/9/Tv//Du
6f/i4Nr/y8nF/6GZj/+Mc1r/vKGH/8uul/++n4T/
noBm/4JyZf+yrqf/zcvC/+Hb0f/r5dv/7ufc/+7m
3P/u5Nv/7ePa/+zk2f/r4dj/6eLW/+nh1f/o4NT/
6d/T/+je0v/o3dH/5NnN/9DGuv/Tyr//6uPY/+zm
3P/s5tr/7OXa/+vj2f/r49n/6ePX/+ri1//q39b/
6uDX/+ng1f/o3tX/6N/U/+rf0//n39P/59/T/+fd
0f/o3dD/5t3Q/+fc0P/m28//5trN/+Xazf/k2cz/
5NjM/+TZzP/j2Mv/49jL/+HXyv/h1sn/4NXI/+DU
yP/f08f/3tPG/97SxP/c0cT/28/C/9vOwf/azsH/
2M2//9bLvv/Vyr3/1Mm8/9PIuv/EtqX/X1JF/1VJ
Pv9oRi7/bUox/2pIL/9dPSf/SC8c7gcHB4sHBwdq
BwcHRgcHBygHBwcTBwcHBgAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
UjYeXW1JL+qPZ0n/nnla/5NwUP+UclT/so9x/8Ge
fv+lloj/pJmL/6CQgP/u7Ob///78///+/P/+/vz/
/v36//79+v/+/fr//f37//38+f/9/Pn//fr4//z7
9//8+/f//Pn3//v69v/7+fX/+/f0//j38f/z8ez/
6OTh/9LQy/+xrqn/gmZR/7aYf//MsJj/xKaK/6yO
cv93X03/qqWi/8nEvv/e2dH/6+Tb/+7o4P/u6eD/
7uje/+7n3P/t5tv/7OTa/+zi2f/r49j/6uLX/+rh
1v/p4dX/6eDT/+jf0v/k287/0Me6/9TJwP/r49n/
7ufc/+7m2//s5tv/7Oba/+zl2v/r5dn/6uPY/+ni
1//p4df/6+LX/+nh1//o4NX/6N7V/+ff1P/o39L/
59/T/+fe0//o3dH/6N7R/+fc0P/m3M7/5dvO/+Xa
zf/l2s7/5drN/+PazP/j2cr/49jL/+LXyv/h1sn/
4NXI/+DUyP/e1Mf/3dPG/97SxP/c0cT/3M/D/9rO
w//azsH/2c3A/9fLvv/Vy73/1cq8/8S2pv9fUkX/
Vkk+/2dHL/9uSjL/akgv/14+KP9ILxzuBwcHigcH
B2kHBwdFBwcHKAcHBxMHBwcFAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AABSNh5dbUkv6o9nSf+ge1r/k3BQ/5RzVv+0kXH/
wp5+/6aXif+lmYz/oZSD/+/t6P///v3///78//7+
/P///v3//v78//7+/P/+/fr//v36//79+v/+/fn/
/fz5//36+P/8+/f//Pv3//v69v/6+PT/9/Pw/+3r
5//Z19P/vry4/3pjUP+vkXX/y7CX/8eokP+1lnv/
g2ZR/6Cblf/Dvrn/29bP/+rk3f/v6+P/8Ovj/+/q
4f/u6eD/7uje/+7o3v/t5tz/7Obb/+zl2v/r5Nn/
6+PX/+ri1v/p4NX/6eDV/+bb0P/Sx7v/1czB/+vk
2//u6N3/7ufd/+7m3P/u5tz/7ubb/+3l2//s5dr/
7OTa/+rj2P/p49f/6uTX/+ri1//p4df/6ODV/+rf
1P/q39T/6ODU/+ff1P/o3tH/6d/R/+fd0P/m3M//
5tzQ/+bczv/m28//5NrN/+Tazf/j2cv/5NjL/+PX
y//h18n/4NXI/+DVyP/f1cj/3dLH/93Rxf/c0sT/
3NDD/9rPw//azsL/2c2//9bLv//XzL//xbin/15R
RP9XST7/aUgv/29LMv9rSDD/Xj4n/0guHO0HBweJ
BwcHaAcHB0QHBwcoBwcHEwcHBwUAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAFI2Hl1tSS/qj2dJ/6B7Wv+TcFD/lXRX/7SS
cf/DoH//ppmK/6abjf+ilIT/8Ozp///+/f/+/vz/
//79/////f///vz//v78//79/f/+/fz//v38//79
+v/9/Pv//fz5//38+f/8+/j//Pn3//n38//w7ez/
4N3b/8bDwf+FdGb/pYZr/8epk//KrJT/vZyB/5Z5
YP+Ngnv/urey/9bRzP/p493/7+rk//Pt5v/x7eT/
8Ozk//Hr4//v6uL/7+jh/+7n3f/u5d3/7ebb/+zl
2v/r5Nr/6+PY/+ri1//p4tb/5d3R/9LIvP/WzMP/
7Obc/+/p4f/u6N7/7ujd/+7o3f/u59z/7ubc/+3m
2//t5tv/7OXa/+zk2f/r49j/6uLY/+rj2P/q49f/
6eHW/+jg1f/o4NT/6uDT/+ng0//o3tL/6d/R/+fd
0f/p3dH/593Q/+bbz//l28//5dvO/+Xbzf/j2cz/
5NnM/+PYy//j2Mr/4NbJ/+DVyP/g1cj/39PI/97T
xv/e0sb/3NDE/9rPwv/az8L/2M3B/9bLv//GuKj/
XlBE/1dJPv9qSC//cEwy/2tIMP9ePij/RSwb5wcH
B4gHBwdnBwcHQwcHBycHBwcSBwcHBQAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAVDYeXW1JL+qPZ0n/oHta/5RwUP+WdFb/
tZJy/8SggP+omor/p5yO/6SUhf/x7Or///79////
/f////3////9///+/f///v3///79///+/P/+/vz/
/v38//79+v/9/fv//fz5//38+f/6+fb/8/Lu/+Xi
4P/NzMn/mY6F/5Z7Yf/BpIv/zLCX/8Gjhf+piG7/
fmpa/7Gvq//QzMn/5eHb/+7s5v/z7+j/8+7o//Pt
5//y7Ob/8ezl//Dr4//v6uL/7+nh/+/p3v/u593/
7ubc/+3m3P/t49r/6+PY/+rj1//m3tL/0cm9/9fP
xf/t593/7+ri/+/p4f/v6eH/7+je/+/n3f/u6N3/
7ufc/+7n3P/u5tv/7OXa/+zl2v/r49j/6+PY/+zk
2P/q49j/6uPX/+rh1v/p4dX/6uDU/+jg1P/p39P/
6d7S/+ff0//o3tH/6N3Q/+bb0P/m28//5dvO/+Xb
zf/k2s3/5NrN/+PYy//i18r/4dfK/+HVyP/h1cj/
39TH/9/Tx//d0sf/3NHE/9vRxP/bzsL/2c3C/8W5
qP9eUET/V0o9/2tJMP9xTTP/bUkx/14+KP9FLRvm
BwcHiAcHB2cHBwdDBwcHJgcHBxIHBwcFAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAABSNh5dbUkv6o1nSf+ge1r/lHBQ/5d0
Vv+3k3T/xKGA/6ibi/+onI//pJeH//Ht6/////3/
///9/////f////7////+///+/f///v3///79//7+
/f/+/v3//v78//79/P/9/fv//Pv6//b18v/r6uf/
09LR/62qpf+IbVT/vJ+E/82xm//Fp43/s5R4/3xg
TP+qp6X/ycfC/+Pe2f/u7Ob/9O/s//Xx6//18Or/
9O/p//Pt5//y7eb/8e3l//Hs5P/w6+L/7+nh/+7o
4P/u597/7uXd/+3m3P/s5dv/7OTZ/+fg1P/Syr7/
2dLI/+7o4f/w7OP/8Ovj//Dq4v/v6uL/7+jh/+/p
3v/u597/7ujd/+7l3f/u5tz/7ebb/+3l2v/s5dr/
6+TZ/+zj2P/r5Nn/7OTY/+vi1//p4tX/7ODV/+ng
1f/q4NT/6N7S/+nf0v/o3tL/6N3R/+Xc0f/n3dH/
59zQ/+Xczv/l287/5NrO/+PYzP/i2Mr/4dfL/+HW
yf/h1cj/4NXI/9/Tx//e0sf/3dHF/9zQw//bz8P/
xrmq/19SRf9ZST3/bEox/3JNNP9tSjD/Xj4o/0Qs
GuUHBweHBwcHZQcHB0IHBwclBwcHEQcHBwQAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAFI2Hl1tSS/qj2hJ/6B7Wv+UcFH/
l3RZ/7eTdP/Fo4L/qJuM/6idkP+ml4n/8u7s////
/f////3////+/////v////7///7+///+/v///v7/
//79//7+/f/+/v3//v78//38+//5+PX/7u3t/9nY
1/+9vLv/fmNP/7OXe//OsZr/yaqR/7ycf/+NcVj/
mpWP/8K/vf/d2db/7Ovl//Px7P/38+3/9vLs//bw
7P/18Ov/9O7p//Pu6P/y7ef/8u3m//Hs5f/x6+T/
8Ori/+/q4f/u6d7/7uje/+3m3P/t5dv/6eHW/9PK
v//b08n/7+ri//Ht5f/x7OT/8evj//Dr4//w6uL/
7+ni/+/p4f/u6OD/7ujd/+7o3f/u593/7ufc/+7m
2//t5dr/7OTa/+zk2P/u5Nj/7OTZ/+zj2P/s4tb/
6+LV/+rh1P/p4dX/6uDU/+rg0v/n3tP/597T/+jd
0v/m3dL/593Q/+bdz//l3M//49rP/+PZzf/k2cz/
4tjL/+HXyf/h1sn/4NXI/97UyP/f0sf/3NHF/9zQ
xP/Huan/YFNG/15OQf9vTTP/c08z/25LMf9gPyj/
QSoZ4AcHB4YHBwdkBwcHQQcHByUHBwcRBwcHBAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAVDYeXW1JL+qPaEn/oHla/5Nw
Uf+YdVj/t5R1/8ajg/+om4z/qJ6Q/6eaiv/y8Oz/
///9/////v////7////+/////v////7////+////
/v////7///7+///+/f/+/v3/+vr4//Hx8P/g4N7/
xcTD/4BqW/+rjnT/y62X/8yulv/Bo4X/ooNo/4Z4
bP+6ubb/1tXR/+ro5P/18u3/9/Tv//j17v/38+3/
9vLs//by7P/18ev/9PDq//Tv6f/z7uj/8u3n//Ht
5v/x7OT/8Ovj/+/q4f/u6eH/7uje/+7n3f/q4tj/
1MzC/9zTy//v6+T/8+3m//Lt5f/x7eX/8e3k//Hr
4//w6+L/8Ori//Dp4v/v6eH/7ujg/+7o3f/u593/
7ufc/+7m2//t5tv/7OTZ/+zk2f/r5Nj/7OTZ/+zj
2P/r4tf/6uHW/+ri1v/r4dX/6eDV/+rf1P/q4NT/
597T/+fe0//n3dH/593R/+bc0P/l3M//5drO/+TZ
zP/k2cz/49jL/+LXy//h1sn/4dTJ/9/TyP/f08j/
3tLG/8O2pf9QRTz/YE9B/3FONP90UDT/b0sy/2A+
Kf9BKhnfBwcHhQcHB2QHBwdABwcHJQcHBxAHBwcE
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAABUNh5dbUkv6o9oSf+geVr/
lHFR/5h1V/+3lXb/x6SD/6icjv+pnpH/qJyM//Pv
7P////3////+/////v////7////+/////v////7/
///+/////v////7///7+//z8+//19PP/5eXk/8zL
yv+Qg3f/oYJq/8apkf/Ospr/xqWL/7CRdf96Y1H/
sbCv/9HOzP/n5uL/8/Ht//j28v/59fL/+Pbx//f1
8P/49O7/9vHu//fy7P/28ez/9fDr//Xv6v/07un/
8+3o//Pt5v/y7OX/8evj//Dr4//v6uL/7une/+vi
2v/WzMT/3tXN//Hs5f/07uj/9O3n//Pt5v/y7eb/
8e3l//Hs5P/w7OP/8Ovj/+/q4v/w6eD/7unh/+/o
3//u5+D/7ufe/+7n3f/u593/7ubb/+zl2//s5Nr/
7eXZ/+zk2f/r49j/6+PY/+ri1//q4Nf/6d/W/+rf
1v/o4NT/59/T/+nf0//p3dL/5d7R/+fd0P/m3c//
49vP/+bbz//l2s7/49nL/+LXy//j1sr/4NTJ/+HV
yP/g1Mf/wrSj/0xCOv9iT0L/c081/3ZRNf9wTDP/
YUEp/0ApGt4HBweFBwcHYwcHB0AHBwckBwcHEAcH
BwQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAFQ2Hl1tSS/qj2hJ/6B5
Wv+XdFT/mHVX/7iUdf/HpIP/qZ2N/6mfkf+nmor/
8vDs/////f////7////+/////v////7////+////
/v////7////+/////v/+/v3/9/f2/+rq6f/R0dD/
pZ+Z/5N3Xf/BpIn/z7We/8iqjv+6m37/hGhS/6em
o//Kysj/4+Le//Lv7f/59/P/+vj0//n29P/59/L/
+fbx//j18P/59e//+PTu//fz7f/28uz/9PHs//Xw
6//07+n/8+7o//Lt5//y7eb/8uzl//Dr5P/w6uL/
7OXc/9fOxv/g2dD/8+3n//Xw6v/07+n/8+7o//Pt
5//z7ef/8u3m//Hs5f/w7OT/8Ozj//Hr4//w6+L/
7+rh/+/o4f/u6OD/7ujg/+7n3v/u593/7ufc/+3l
2//t49r/7OTa/+3j2//t49r/6+PZ/+vh2P/r49j/
6uDX/+rh1v/q4NT/6eDV/+jg1f/n39P/6N/S/+Xe
0f/l3dH/5tzP/+Xazv/m2c7/5NjN/+PYy//i18v/
4tbJ/+DUyP/CtKT/TEI6/2JQQv90UDb/d1I2/3FN
M/9jQSn/PicY2QcHB4QHBwdiBwcHPwcHByQHBwcQ
BwcHBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAVDYeXW1JL+qPaEn/
oHla/5dzVP+XdVb/uJV1/8mmg/+pnY//qp+R/6OT
hP/x7ev////9/////v////7////+/////v////7/
///+/////v////7//v7+//n5+P/t7e3/2NjX/7e0
s/+Ha1X/up2D/8+2nv/LrpX/waKG/5l7Yf+Ui4P/
wsHA/97d2v/v7+3/+PX0//v49//7+fX/+vj0//r4
9P/59/P/+Pby//j08f/38/D/9/Tv//bz7v/38u3/
9vLs//bx6//z8Ov/9O/p//Pu6P/z7ef/8ezm//Hr
5P/t59//2dDI/+Lc0v/z7uj/9fHr//Xw6//18Or/
9O/o//Pu6P/z7ef/8+3n//Lt5v/x7eX/8ezk//Hs
4//w6+P/8Ovi/+/q4f/v6t//7+nf/+7p4P/u6N7/
7ujd/+7n3f/t5tv/7eXa/+3m2v/s5tr/6+TZ/+vk
2P/q49f/6uLX/+ri1//p4dX/6eHW/+jh1P/n4NP/
6N/S/+je0v/n3dD/59zR/+baz//l2c3/5drN/+PY
zf/i18v/4dfK/8S0pf9NQjr/Y1FB/3ZSNv95Uzb/
ck41/2JBKv8+KRjYBwcHgwcHB2EHBwc+BwcHIwcH
BxAHBwcEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAABSNh5dbUkv6o9o
Sf+helr/mHRU/5d1V/+7lnX/yKWE/6mdjf+qn5H/
o5OF//Dt6/////7////+/////v////7////+////
/v////////////7+/v/7+vr/8fHw/97e3f/CwsL/
fWRR/7WWfv/PtZ7/zrKZ/8Wmiv+qjHL/g3Bg/7m4
uP/X1tX/7ezr//j39P/7+vf//Pv4//z59//7+vb/
+/n1//r49P/59vT/+ffz//n18v/49PH/9/Xw//b0
7v/28+7/9/Ls//Tx7P/08ez/9e/q//Pu6f/z7ej/
8+3m/+7p4f/a08n/5N7W//Pu6//28ez/9vHs//Xx
6//18Ov/9fDq//Tv6P/z7ej/8+3n//Pt5v/y7eb/
8uzl//Hs5P/w7OX/8Ovj/+/r4v/w6uL/7+rf/+7q
4P/u6eD/7uje/+7o3f/t5tz/7Obc/+3l2//t5tv/
7OXa/+vk2f/r5Nj/6+PX/+rj1//p4tX/6eLW/+ni
1f/o39T/59/U/+je0v/n3NH/59zR/+fc0f/l2s//
5drO/+PYzP/j2Mv/xLam/01DOv9jUkD/d1I2/3pV
N/90UDT/Y0Ir/z0nGNcHBweCBwcHYQcHBz0HBwci
BwcHEAcHBwQAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAFQ2Hl1tSS/q
j2dJ/6B5Wv+YdFT/mXZX/7qWdv/JpYX/qZ2N/6qg
kv+jlIb/8e3r/////v////7////+/////v////7/
/////////////////f39//X19f/k5OT/ysrJ/4h3
af+rjXX/zbCY/8+2oP/LqpD/uJp+/3xkTv+vr67/
0NDP/+no5//29fT//fz5//38+f/9/Pj//Pv4//z5
9//8+vb/+/j2//v59f/6+PT/+vb0//n38v/59vH/
+PTx//f18P/39O//9vPu//fy7P/28ez/9fHr//Tv
6v/z7uj/8Ovk/93UzP/m4Nn/9vHs//fz7f/38uz/
9vLs//bx7P/28Ov/9fHq//Xw6v/07uj/8+7o//Pt
6P/z7ef/8+3m//Ls5f/y7OX/8ezk//Hr4//x6+P/
8Orj//Dq4v/v6eH/7+jf/+7p4P/u6OD/7uXd/+7m
3P/u5tz/7ebc/+zk2v/r5Nr/6+PZ/+ri1//q49j/
6uLW/+nh1f/p4NX/6ODU/+fe0//o3dL/59zR/+fc
0P/n287/5drO/+TZzv/Et6f/TUM6/2VSQv95VDf/
e1Y4/3RQNv9lQyv/OSQX0gcHB4IHBwdgBwcHPQcH
ByIHBwcPBwcHBAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVDYeXW1J
L+qPZ0n/oHla/5h0Vf+Zdlf/upd3/8unhf+pnY//
qqCS/6OWh//x7ev////+/////v////7////+////
//////////////7+/v/5+Pj/7e3s/9XV1f+flY3/
n4Jq/8erk//SuaL/zK6W/7+hh/+OdFz/oJyZ/8nI
yP/j4+L/8/Py//v6+f/+/fz//fz7//38+//9/Pn/
/Pv4//z79//7+vf/+/r2//v49v/6+fX/+vj0//n2
9P/59/L/+fXy//j08f/38/D/9vLv//bz7v/28uz/
9vHs//Pw6//w7Ob/3tjQ/+nj3P/38+3/+PTu//j0
7v/28+7/9vLs//by7P/08ez/9PHs//Xw6//08Or/
9O/o//Tu5//07uf/8+3n//Pt5v/z7eX/8u3l//Hs
5P/x7OP/8Ovj//Dr4//w6uD/8Ori/+/p4f/v6N//
7ufd/+7n3P/u5tz/7ufd/+7m3P/s49v/7OTa/+zh
2P/r49n/6+DX/+ri2P/o4db/6ODV/+jf1P/n3tP/
6N7S/+fc0f/n3ND/5tvQ/8a4qP9ORDv/ZVFA/3pV
OP99Vzn/dlA2/2VDK/85JBbRBwcHgQcHB14HBwc9
BwcHIgcHBw8HBwcDAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABSNh5d
bUkv6o1nSf+geVr/mHVV/5p3WP+7mHn/yqeG/6qd
jv+roJL/o5aH//Ht6/////7////+/////v////7/
/////////////////v7+//X19P/i4uL/uLSx/5B2
Xv/Dp47/07uk/861nf/GqI//pIZv/4uAeP+/v7//
3Nzb/+/v7v/6+vn//f38//79/P/+/fz//f37//39
+//9/Pn//fz4//z7+P/8+/f/+/r3//v49v/7+fX/
+vn1//r49P/69vP/+ffy//j28f/49fD/9/Tv//bz
7v/18+3/9PHs//Lt6P/g2tP/6uXf//j07v/69vD/
+fXv//j07v/48+3/9/Lt//by7P/28uz/9vHs//Xx
6//18Or/9fDp//Tv6f/07uj/8+/o//Pu5//y7ef/
8u3m//Lt5v/x7eX/8ezk//Ds5P/x7OP/8Ovj/+/r
4//v6uH/7+nf/+7o4P/u6N3/7ujc/+7n3P/u5tz/
7ePa/+zk2v/s5Nn/6+PZ/+vj2P/q4Nf/6uDX/+jh
1f/n39P/59/T/+jd0v/l3NH/xrmp/05EO/9mUD7/
e1Y4/4BZOv93Uzb/ZkQs/zYjFs8HBweBBwcHXgcH
BzwHBwchBwcHDgcHBwMAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFQ2
Hl1tSS/qj2dJ/6B5Wv+YdFX/mndY/7uYeP/MqIb/
q56N/6ugkv+jlof/8e7s/////v////7////+////
/v/////////////////7+/v/7e3t/9XV1P+DaFT/
vqKJ/9S7pP/SuKL/zK+W/7WYfv9+aVj/tra1/9XV
1P/t7ez/+Pj3//79/P/+/v3//v79//7+/f/+/fz/
/v38//39+//9/Pn//fz5//z7+P/8+/j//Pv3//z5
9//7+vb/+/j2//v39f/6+PT/+ffz//n38//49vH/
+PXw//f07//28e7/8u3q/+Lc1f/s5+H/9/Xw//n3
8v/59vH/+PXw//n17//49O7/9vPu//fy7f/28uz/
9vHs//bx6//18ev/9fDq//Xv6v/08On/9O7o//Tu
6P/z7uj/8+3n//Lt5//y7eb/8uzl//Hs5P/x7OT/
8evj//Dr4v/w6uL/7+rh/+7o4P/u6N7/7ujd/+7o
3v/u6Nz/7ubc/+3l2//t5dr/6+TZ/+vh2P/r4tf/
6uHW/+nh1f/o4dT/6N/U/+be0v/Iu6r/T0U8/2ZS
QP99Vzn/gVo7/3lUNv9mRCz/NCEWygcHB4AHBwdd
BwcHOwcHByEHBwcOBwcHAwAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
UjYeXW1JL+qPZ0n/oHla/5h0Vf+ad1r/vJl5/82o
h/+rno3/q6CS/6SVh//x7uz////+/////v////7/
///+/////////////v7+//b19f/k4+P/p5yU/6KG
bv/RtqL/1byl/861nP/Ao4r/h2tV/6ysrP/Nzc3/
5+fn//b29v/9/fz///7+//7+/v/+/v3//v79//7+
/P/+/fz//f38//39/P/9/Pv//fz7//38+f/8+/r/
/Pv4//z7+P/8+ff/+/r2//v59f/69/X/+vj0//n3
8//59fL/+PTx//f07//z7+z/5N7X/+7q5P/49vL/
+fjy//n38v/59fL/+vXw//n17//39O//+PPu//bz
7v/18+3/9/Ls//bx7P/08ez/9PHs//Xw6//18Ov/
9fDq//Xv6v/07+n/9O7o//Pu6P/07uf/8+3n//Lt
5v/y7eX/8e3l//Ls5f/x6+T/8Orj//Dq4P/u6eD/
7uje/+7n3v/u6N7/7ufe/+3m3P/t5tv/7OTa/+zk
2f/r49j/6uLX/+vh1f/o3tX/59/U/8i7q/9QRj3/
Z1A+/35ZO/+DWzz/elU3/2hGLv80IhbKBwcHfwcH
B1wHBwc6BwcHIAcHBw0HBwcDAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AABUNh5dbUkv6o9nSf+felv/mHRV/5t4Wv+7mHj/
zKeI/6uejf+roJL/pJWH//Hu7P////7////+////
/v////7///////7+/v/5+fn/7e3t/9XV1f+jnZf/
qpN//9K4pP/Ptp7/yayU/5yBaP+dl5L/x8fH/+Hh
4f/x8fH//Pz8/////v///v7///7+///+/v/+/v3/
/v79//7+/f/+/fz//v38//79/P/9/Pv//fz7//38
+//8/Pr//Pv6//z7+P/8+/j/+/r3//v49v/6+fb/
+vf1//n38//49vL/+PTx//Xw7f/m4Nr/7uzn//n3
8//79/T/+vj0//n38v/59/L/+fbx//j18P/49fD/
9/Tv//j07v/48+7/9/Pt//fz7f/38uz/9vLs//by
7P/28ev/9vDr//Xw6//z8Ov/9e/q//Tv6f/07un/
8+3o//Lt6P/y7ef/8u3m//Ht5f/y7eX/8ezj//Dr
4//w6uL/7ujg/+7o3v/u597/7uje/+3m3P/t5tz/
7eXa/+vk2f/s49j/6+HY/+ri2P/p4dX/yrut/1FI
Pf9nUD3/gFs8/4RcPf97Vjn/aEYu/zMhFcgHBwd/
BwcHWwcHBzoHBwcfBwcHDQcHBwMAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAFQ2Hl1tSS/qj2hJ/597W/+bd1f/m3ha/7yZ
ef/OqYj/q56N/6ugkv+klYf/8e7s/////v////7/
///+/////v/+/v7/+/v7//Dw8P/e3t7/wMC//19O
Qv+pjXf/zrKa/8uynP+xl3//jH1w/8TEw//c3Nv/
7+/v//r5+f/+/v7////+/////v////7///7+///+
/v/+/v3//v79//7+/f/+/v3//v38//79/P/9/fz/
/f37//39+//9/Pv//fz5//z7+v/8+/j//Pn4//v6
9//7+Pb/+vn1//n29P/59/P/9fPv/+jj3f/w7On/
+vj0//v59f/69/X/+/f0//r28//69/L/+ffx//r2
8P/49vH/+PXw//n17//49e7/+PTu//j07f/38+3/
9/Lt//by7P/38ez/9vHs//bx7P/18ev/9fHr//Xw
6v/08Or/9O/p//Pv6P/z7uj/8+3n//Lt5v/x7eb/
8e3l//Hs4//w6+P/8Ovi/+/p4f/u6OD/7uje/+7n
3f/u59z/7ebc/+zk2v/r49n/6+HY/+ri1//Lvq//
UUc+/2hRPv+CWzz/hl4+/3xYOv9qRy7/MSAVxAcH
B34HBwdbBwcHOQcHBx8HBwcNBwcHAgAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAVDYeXW1JL+qPZ0n/n3pb/5t3V/+ad1n/
vJp5/86qiP+sno7/q6CS/6SXiP/x7ev////+////
/v////7////+//z8/P/z8/P/4+Pi/8rKyv9vZFv/
emBI/5h6Xf+WfGT/noJt/4JqV//IyMj/3t7e/+3t
7f/4+Pf//v7+///////////////+/////v////7/
///+///+/v///v7//v7+//7+/f/+/v3//v39//79
/P/+/fz//v38//39+//9/Pv//fz7//36+f/8+/r/
/Pv4//v69//7+Pb/+vn1//r49P/39fH/6uXf//Hu
7P/7+Pb//Pr2//v69f/7+fT/+/f0//r49P/69vP/
+vfy//n38f/59vH/+vbw//j28P/48/D/+fXv//f0
7//49O7/+PTt//f07f/38+3/9/Pt//fy7f/38ez/
9vHs//bw6//28ev/9fDq//Xv6v/07+n/9O7o//Pu
5//y7ef/8e3m//Hs5f/x7OT/8ezj//Dr4v/v6eH/
7uje/+7o4P/t593/7ebc/+zl2v/t49r/6+PZ/8y/
sP9SSD//aVA9/4RdPv+HX0D/fVg7/2pIMP8xIBXD
BwcHfQcHB1oHBwc4BwcHHwcHBw0HBwcCAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAABUNh5dbUkv6o9oSf+fe1v/m3dY/5t3
Wf+9mnr/z6uJ/6yfjv+roJL/pZmJ//Ds6v////7/
///+/////v/9/f3/9vb2/+jo5//Pz8//h4B6/3JZ
Qf+efmD/d11F/3VqYf+tqab/ycjF/+Li4v/v7+//
+Pj4//39/f/////////////////////////+////
/v////7///7+///+/v///v7//v7+//7+/f/+/v3/
/v79//79/f/+/fz//v38//39/P/9/fv//fz7//38
+//8+/r//Pv4//v69//7+Pf/+vn1//f28v/s5+L/
8+/s//v69v/8+ff//Pv3//z69v/7+Pb/+/n1//r5
9P/6+PP/+vbz//n48v/59/L/+ffy//n28f/69fD/
+PXw//f18P/39fD/9/Xv//f07//49O7/+PPu//jz
7v/38+3/9/Lt//by7P/28ez/9vHr//Xw6v/17+r/
9O/p//Tu6f/z7uj/8+7m//Lt5v/x7OX/8ezl//Dr
4//w6+L/7+nh/+/o4f/u597/7ufd/+3m3P/s5Nr/
zMCz/1NJQP9qUDz/hV4//4lgQf9/Wjv/a0kw/y8g
Fb8HBwd8BwcHWQcHBzgHBwcfBwcHDQcHBwIAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAFI2Hl1tSS/qj2hJ/597W/+ceFj/
m3dZ/72aev/Pq4n/rJ+O/6ugkv+jl4f/7u3o////
/v////7//v79//r6+f/t7e3/2NjX/6aioP9qUzz/
nX5g/4dqUP9gT0L/sbGw/8/Pz//m5ub/8vLx//r6
+v/9/f3/////////////////////////////////
/////////v////7////+///+/v///v7///7+//7+
/f/+/v3//v79//7+/f/+/v3//v38//79/P/9/fz/
/f37//38+//9/Pn//Pv4//z5+P/7+Pf/+Pfz/+zn
5P/08u7//Pn3//z7+P/8+/f//Pv3//z59//7+vb/
+/n1//v59f/6+PT/+vj0//r28//69/L/+ffy//n3
8v/59/L/+ffy//n28f/59PH/+PXw//j18P/49fD/
9/Tv//j07v/28+7/9/Tt//fz7f/28uz/9vLs//Tx
7P/08ez/9PDq//Tv6v/07+j/9O7o//Pt5//y7eb/
8ezl//Ds5f/w7OP/7+ri/+/p4f/u6eH/7uje/+7m
3P/NwrT/U0tB/2tSPP+HX0D/imJD/4BbPP9sSjD/
LR0UvAcHB3wHBwdYBwcHNwcHBx4HBwcMBwcHAgAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAUjYeXW1JL+qNZ0n/n3pb/5x3
WP+beVr/vpt7/9Csiv+sno7/q6CS/6OXh//t6+b/
///+/////v/+/v3/9fX1/+Xl5P/FxMP/ZVFA/5d4
W/+WeVv/Yks4/56bmf/Kysr/5OTk//T09P/8/Pz/
////////////////////////////////////////
/////////////////v////7////+/////v///v7/
//7+//7+/v/+/v7//v79//7+/f/+/v3//v39//79
/f/+/fz//f38//38+//9/Pn//Pv4//v69//59vT/
7enm//bz8f/8+/j//fz4//38+P/8+/j//Pv3//z5
9//7+vb/+/j2//v59f/79/X/+/f1//v39P/6+PT/
+fj0//n49P/69/L/+vbz//n38//49/L/+Pby//j2
8f/49vH/+PTx//j18P/38/D/9/Tv//jz7v/28+7/
9/Pt//bx7P/28ez/9O/s//Pw6//07+r/9O7p//Pu
6P/z7ef/8u3m//Hs5f/x7OP/8Ovj//Dq4v/v6eH/
7uje/87Dtv9UTEH/alE5/4hfQv+KYkP/gVs9/21K
Mv8tHRS8BwcHfAcHB1gHBwc3BwcHHQcHBwwHBwcC
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAABUNh5dbUkv6o1nSf+felv/
nHdY/5x5Wv++nHv/z6uM/6yfjv+roJL/o5eH/+3p
5v////7////+//39/f/z8/L/3t7e/3ZkWP+Qclb/
oYJk/3JZQv+Adm//wcHB/93d3f/w8PD/+/v7////
////////////////////////////////////////
/////////////////////////v////7////+////
/v////7///7+///+/v/+/v7//v7+//7+/f/+/v3/
/v79//79/P/+/fz//f38//38+//9/Pn//Pv4//r5
9f/u7Of/9/Ty//38+f/9/Pv//fz5//38+f/8+/j/
/Pv3//z79//8+ff//Pr2//v49v/7+vb/+/n1//r5
9f/6+fX/+vj0//r49P/6+PT/+vjz//n49P/5+PP/
+ffz//n38//59/L/+fbx//j28f/39vD/9/Xw//n1
7//39O//+PPu//fy7f/38uz/9vHs//Xw6//z8Ov/
9PDq//Pu6f/07un/8+3m//Lt5v/x7OX/8evk//Dr
4//v6uH/0MW5/1VLQv9sUDr/iWFD/4xjRP+EXT7/
bksy/yobE7gHBwd7BwcHVwcHBzYHBwcdBwcHCwcH
BwEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAFQ2Hl1tSS/qj2hJ/596
W/+cd1j/nHla/8CcfP/PrIz/rZ+O/6ugkv+jl4f/
7enm/////v////7//f39//Pz8v+dkon/f2FI/6eG
Z/+DZUz/aVhL/7u7uv/V1dX/7Ozs//j4+P/+/v7/
////////////////////////////////////////
//////////////////////////////////////7/
///+/////v////7////+///+/v/+/v7//v7+//7+
/v/+/v3//v79//79/f/+/fz//f38//38+//8+/r/
+vn2/+/t6f/49fP//fz7//77+v/9/Pn//fz5//36
+f/8/Pj//Pv4//z79//8+/f//Pv3//z59//8+vb/
+/r2//v69v/7+fX/+/j2//v59f/6+fX/+vn1//r5
9P/6+PT/+vj0//n49P/5+PP/+ffz//n38v/49vH/
+PTx//j18P/39fD/9/Tv//fz7f/38+3/9/Lt//bx
7P/08ez/8/Dr//Tv6v/07un/8+7o//Lt5v/y7OX/
8ezl//Dr4v/RyLr/VU1D/2xQOP+IYkT/jmZG/4Zf
Pv9vSzP/KRoTtgcHB3oHBwdWBwcHNQcHBxwHBwcL
BwcHAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAVDYeXW1JL+qQZ0n/
oXpb/5x4WP+deVr/wZ17/8+sjP+tn47/q6CS/6OX
h//t6uX////+/////v/+/v3/9fX0/6Wbk/+BY0r/
i25U/2ZPPf+4t7T/09PT/+fn5//19fX//f39////
////////////////////////////////////////
////////////////////////////////////////
//////7////+/////v////7///7+///+/v///v7/
/v7+//7+/v/+/v3//v79//79/f/9/fz//fz7//38
+//7+vf/8Ozq//j39P/++/r//v36//79+v/++/n/
/vv5//38+f/9+vj//Pv4//z7+P/8+/j//Pv3//z5
9//8+ff//Pn3//z59//8+vb//Pr2//z69v/7+Pb/
+/j2//v49v/7+fX/+/n1//r59P/6+PT/+fjz//n3
8//59fL/+fXy//j28f/49PH/9/Pw//f07//49O7/
9/Pt//fy7P/28uz/9fHr//Xw6//07+r/9O7o//Pt
5//y7eX/8evk/9PJvP9WTET/bVA3/4tkRf+QZkf/
hl9A/29NM/8pHBO2BwcHeQcHB1UHBwc0BwcHHAcH
BwsHBwcBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAABUNh5dbUkv6o9n
Sf+hfFv/nHlY/516Wv/AnXz/0K+M/62fjv+roJL/
o5eH/+3o5f////7////+//7+/f/5+fj/6+rp/3tr
Xf9jSzn/rKah/97e3v/p6en/9PTz//v7+///////
////////////////////////////////////////
////////////////////////////////////////
///////////////////+/////v////7////+///+
/v///v7//v7+//7+/f/+/v3//v79//79/P/9/fz/
/fz7//v69//w7Or/+fj1//79/P/+/fz//v38//79
+v/9/fv//v36//38+f/9/Pn//fr4//38+f/9/Pj/
/fr4//z7+P/8+/j//Pv4//z7+P/8+/j//Pv3//z7
9//8+ff//Pn3//v69//7+vb/+/j2//v59f/6+fX/
+vf1//r49P/69vP/+ffz//n18v/49vH/+PTx//f1
8P/39e//9vTu//bz7v/18u3/9vHs//Xx6//17+r/
9O/o//Pt6P/z7eb/08q//1ZORP9uUDf/jGRF/5Fo
SP+IX0L/cE4z/yMYEbAHBwd5BwcHVQcHBzQHBwcc
BwcHCgcHBwEAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAFQ2Hl1tSS/q
kGdJ/6F6W/+gfFr/nHla/8CcfP/Qr4z/rZ+O/6ug
kv+kl4f/7unk/////f////7////+//39/f/4+Pf/
8vLy/+zr6v/t7e3/8PDw//X19P/7+/v//v7+////
////////////////////////////////////////
////////////////////////////////////////
///////////////////////////+/////v////7/
///+///+/v///v7//v7+//7+/f/+/v3//v38//79
/P/9/Pv/+vn4//Ds6//5+PX//v38//7+/P/+/fz/
/v38//79+v/+/fr//f37//39+//9/Pn//fz5//38
+f/9/Pn//fz5//z8+v/8/Pr//fz5//z7+v/8+/j/
/Pv6//z7+P/8+/j//Pv4//z7+P/7+vf//Pn3//v6
9v/7+Pb/+/j2//r59f/6+PT/+vj0//n38//59/L/
+Pbx//j08f/38/D/9vTv//j07v/38u3/9vLs//bx
7P/18Ov/9O/p//Pt6P/VycH/V01F/29QN/+NZUb/
k2lJ/4lhQv9xTTT/IxgRrgcHB3kHBwdUBwcHNAcH
BxsHBwcKBwcHAQAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVDYeXWxI
L+qNZUf/n3dY/555WP+celr/wZ17/9Gujf+tn47/
q6CS/6SXh//s6eT////9/////v////7////+//7+
/v/8/Pz/+/v7//r6+v/7+/v//f39//7+/v//////
////////////////////////////////////////
////////////////////////////////////////
//////////////////////////////7////+////
/v////7///7+///+/v/+/v7//v79//7+/f/+/fz/
/f38//38+//6+fj/8Ozq//n49f/+/vz//v78//7+
/f/+/fz//v36//79+v/+/fr//v36//79+v/9/Pv/
/fz7//38+//9/Pv//fz7//38+f/9/Pn//fz7//38
+f/9/Pn//fz5//38+f/9/Pn//Pv6//z7+P/8+/j/
/Pn3//v69//7+vf/+/j2//v59f/6+fX/+vj0//r4
9P/59/P/+ffy//j28f/49fD/9/Xw//f07//28+7/
9fLt//Tx7P/18er/9O/p/9bLw/9ZT0b/cVM5/45m
SP+Takv/iWFC/3JONP8jGBGuBwcHeAcHB1MHBwcz
BwcHGwcHBwoHBwcBAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABSNSBb
Xz0l13hUN+yHYkTujGlK9Jt5Wv/AnX3/0q6O/62g
jv+roJL/pJeH/+3o4/////3////+/////v////7/
///+////////////////////////////////////
////////////////////////////////////////
////////////////////////////////////////
/////////////////////////////////v////7/
///+/////v////7///7+///+/v/+/v3//v79//79
/P/9/fz//fz7//r59v/u7Oj/+fj1//79/P///v3/
//78///+/P/+/vz//v78//7+/P/+/fz//v36//79
+v/+/fr//v36//39+//9/fv//v36//39+//9/fv/
/fz7//38+//9/Pv//fz7//38+//9/Pn//fz5//36
+f/8/Pj//Pv4//z7+P/8+ff/+/r3//v69v/7+Pb/
+vn2//r39f/6+PT/+ffz//n18v/49vH/+PXw//n0
7//29O7/9fLt//by7P/17+r/1cvC/1xSSf94Vz3/
kmpK/5VsS/+KYkT/c1Az/x4WEKgHBwd3BwcHUgcH
BzIHBwcaBwcHCgcHBwEAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFE0
HSVNLxxlVTYfaVs7JXZfQSqinHla/8CffP/TsI3/
r6CN/6ugkv+kmIj/7Oji/////f////7////+////
/v////7////+////////////////////////////
////////////////////////////////////////
////////////////////////////////////////
//////////////////////////////7////+////
/v////7////+///+/v///v7//v79//7+/f/+/fz/
/v38//79+v/9/Pn/+fj0/+3p5v/5+PX///78///+
/f///v3///78//7+/P/+/vz//v78//79/P/+/fr/
/v38//79+v/+/fz//v38//79+v/+/fz//v38//39
/P/9/fv//v38//79+v/+/fz//f37//38+//9/Pv/
/fz7//38+f/8/Pr//Pv6//z7+P/8+/j//Pn4//v6
9//7+vf/+/n1//v39f/69/X/+vj0//n38//59fL/
+PTx//f07//29O7/9/Ls//Tx7P/Syr7/UElC/35d
QP+Xbk3/lm1M/4tiRf9zTzX/HRYQpwcHB3YHBwdS
BwcHMQcHBxkHBwcKBwcHAQAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAABwcHCDUnGyacelr/wJ59/9Sw
jv+woI7/q6CS/6aZif/p5uH////9/////v////7/
///+/////v////7////+/////v//////////////
////////////////////////////////////////
////////////////////////////////////////
//////7////+/////v////7////+/////v////7/
///+/////v////7///7+//7+/f///v3//v79//7+
/P/+/fr//f37//z5+P/19PD/6uXf//j18//+/fz/
///9///+/f///v3///79///+/P///vz///78///+
/P/+/fz//v38//79/P/+/fz//v38//79/P/+/fz/
/v38//79/P/+/fz//v38//79/P/+/fz//v38//79
+v/9/Pv//fz7//38+//9/Pn//Pz6//z7+v/8+/j/
/Pv4//z7+P/7+vf/+/r2//v49v/6+fX/+vj0//n3
8//59/L/+PTx//f07//48+7/9vLs/8/HvP9KQzz/
gV5B/5hvTv+Yb0z/i2ZE/3NQNf8dFhCnBwcHdgcH
B1AHBwcxBwcHGQcHBwkHBwcBAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAHBwcINScbJpx7W//An3z/
0q+O/7Cgjf+roJL/qJyM/+jj3f////3////+////
/v////7////+/////v////7////+/////v////7/
///+/////v////7////+/////v////7////+////
/v////7////+/////v////7////+/////v////7/
///+/////v////7////+/////v////7////+////
/v////7////+/////v///v3//v79//7+/f/+/vz/
/v78//38+//69/X/7uzm/9rRyf/Kv7f/3NXM//Tx
7P/9/Pn//v38//7+/f/+/vz///78///+/P/+/vz/
//78///+/P/+/fz//v78//79/P/+/fz//v38//79
/P/+/fz//v78//7+/P/+/fz//v38//79/P/+/fz/
/v38//79/P/9/fv//fz7//38+//9/Pv//fz5//38
+f/8+/r//Pv4//z7+P/8+ff/+/r2//v49v/6+fX/
+vj0//r28//59fL/+Pbw//n07//38+3/0Mi9/0pD
Pf+CX0L/mnFQ/5lvUP+NZUX/c1A2/xgSDaAHBwd1
BwcHTwcHBzEHBwcZBwcHCQAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAcHBwc2JxolnXpa/8Gd
ff/Sr47/sKCN/6ugkv+qn5H/5N7Y/////f////3/
///+/////v////7////+/////v////7////+////
/v////7////+/////v////7////+/////v////7/
///+/////v////7////+/////v////7////+////
/v////7////+/////v////7////+/////v////7/
///+/////v///v3///79///+/f///v3//v78//38
+f/39PL/7ejj/9bPxv+ploP/p4hs/6OEaP+sjnH/
w7Sm/+fi2//59vT//v78///+/f///vz//v79//7+
/P///vz//v38///+/P/+/vz//v78//7+/P/+/fz/
/v79//79/P/+/fz//v38//7+/P/+/fz//v38//79
/P/+/fz//v38//79/P/9/fv//f37//39+//9/Pv/
/fz5//38+f/8+/r//Pz6//z7+P/8+fj/+/r3//v4
9v/6+fX/+vj0//n38//59vH/+PXw//j07v/Ryb//
SkQ9/4NfQ/+bck//m3FP/49nSP9zUTb/GBINoAcH
B3UHBwdPBwcHMAcHBxgHBwcIAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAABwcHBzYnGiWdelr/
w598/9Sxjv+xoI7/q6CS/6qfkf/h29T///79////
/f////3////+/////v////7////+/////v////7/
///+/////v////7////+/////v////7////+////
/v////7////+/////v////7////+/////v////7/
///+/////v////7////+/////v////7////+////
/v////7////9///+/f/9/fv/+Pfz/+/t6f/n4tz/
3tXO/8W2qf+khm7/qohq/6aDZP+de1z8lHNW+Z58
Xv+qhmj/qY93/83Fuv/l4Nn/8u7s//r59f/+/fn/
/v76//7+/P/+/vz//v78//7+/P///vz//v78///+
/P/+/fz//v38//7+/P/+/vz//v38//79/P/+/fz/
/v38//79/P/+/fz//v38//79/P/+/fz//f37//79
+v/9/Pv//fz7//38+//9/Pn//fz5//z7+P/8+ff/
/Pn3//v69v/6+fX/+vj0//n48//59fL/+fXv/9LK
wP9KRD3/hGFD/51xUf+bc1H/j2hI/3VRN/8YEg2f
BwcHdAcHB04HBwcvBwcHGAcHBwgAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcHOCgbJJx5
Wv/Dnn3/1LGO/7Ggjv+roJL/q6CS/9/Z0v///v3/
///9/////f////3////+/////v////7////+////
/v////7////+/////v////7////+/////v////7/
///+/////v////7////+/////v////7////+////
/f////3///79///+/f/+/fz//Pz6//n49f/08O7/
7Onk/+jj3f/k39n/4NnS/9bQyP+/sKP/pIhv/7CP
cP+zkHH/rotr/6OAYP+QblP7akwzrzEjGEceFxE1
ZkgvnopoTfybeVv/poJl/6SFaP+ql4T/w7ep/87H
u//X0Mf/3NbM/+Da0//o493/8vDs//v69//+/fr/
//78//7+/P///vz//v78//79/P/+/fz//v78//7+
/P/+/fz//v38//79/P/+/fr//v36//79/P/9/fz/
/fz7//38+//9/Pv//fz7//38+f/9/Pn//fr5//z7
+P/8+/j//Pn3//v49v/6+fX/+vj0//n38v/59vH/
1MrB/0pEPf+FYUT/nXRR/5xzUP+PaEj/dVI3/w8M
CpcHBwdzBwcHTQcHBy4HBwcXBwcHBwAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcHBwcWEQ4X
m3hZ/8Gde//UsI3/saCO/6ugkv+roJL/3dbP///+
/f///v3///79/////f////3////9/////f////3/
///9/////f////3////9///+/f///v3///79//79
/P/9/Pn/+/r5//n49f/19PD/8O7q/+rn4v/n4t3/
5uHa/+Pd1//g2dL/3NPL/9fNx//MwbX/vbCj/6iT
f/+rjG7/tJJx/7aRcv+wjW3/rIlq/6eDZP+gfV7/
mXZZ/5BwUv1+XkDYZkkwoTcnGj4HBwcgBwcHGgcH
BxUHBwcTUTklOmpLMrN9Wj/eiWdM/49vUv+XdFf/
nXpb/6J+YP+mg2T/qoZo/6qHav+vnIr/y8O3/9nS
yP/f2dL/5d/Z/+3q5f/29PD//Pv3//79+v/+/fr/
/v38//79/P/+/fz//v38//79/P/+/fr//vv6//79
+v/9/fv//f37//38+//9/Pv//fz5//38+f/9/Pn/
/Pz6//z7+P/7+vf/+/r2//v59f/6+PT/+fjz//n1
8v/VysL/TEU//4ZiRv+edVL/nXVT/5BpSf92Uzb/
DwwKlwcHB3IHBwdMBwcHLgcHBxYHBwcHAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwcHBQcH
BxGbd1n/wZ57/9SwjP+woI3/qqCS/6ugkv/Wz8b/
+vr2//n49f/29PD/9PLt//Pv7P/u7Of/6eTe/+bh
2//m4dv/5uHb/+bh2//m4dv/5N/Y/+Lc1P/g2dL/
3NXM/9HIvf/Lwrf/va2f/7Cciv+pkHn/spFy/7iW
df+5lXX/tJFx/7GObv+siWn/qYVm/6WCYv+ifl7/
nXpa/5l2V/+UcVT/iWZJ4YJfQtd0Vjm1Z0gxlV5C
LG9JNSNGBwcHHgcHBxoHBwcWBwcHEwcHBw4HBwcK
BwcHBwcHBwYHBwcGBwcHBwcHBwsZEw4SVTsnQmBB
K25mRy+WclE3vn5dQOSIZ0r/j2xR/5VyVf+beFr/
n31c/6SBYf+ng2T/pYZr/7aml//Qyb7/3NbO/+Hc
1f/n4tz/7+3o//j18//8+/j//fz7//39+//+/fr/
/vv6//38+f/9/fv//fz7//38+f/9/Pn//fz5//36
+f/8+/r//Pv4//z59//8+ff/+/j2//r59f/6+PP/
+ffy/9TMwv9LRD7/hmJG/6B2VP+fdlL/kmlJ/3ZS
Nv8OCwmTBwcHcAcHB0oHBwcsBwcHFgcHBwcAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcE
BwcHDpp3WP/BnHn/1K+K/8aoi/+qn5H/qqCS/7Wl
lv/Nw7b/zcK1/8KxoP+4ppP/tqKO/7GZgv++n33/
yKaC/8mmg//HpID/w6J//8Ggff++m3v/u5h4/7iU
dP+0kHD/sIxs/6uHaf+phGb/pIFh/6F9Xv+beFr/
l3RW/41rTeiEYkTXfFs+vXNUN6pnSjGNZEYufFpA
Kl5SOydMMCMYKgcHBxsHBwcZBwcHFgcHBxUHBwcT
BwcHEAcHBw8HBwcNBwcHCgcHBwcHBwcGBwcHBAcH
BwIHBwcBBwcHAQcHBwEHBwcBBwcHAgcHBwQHBwcG
BwcHCAcHBwoHBwcNBwcHECkdFRpROSVEXkEpcmRH
LppyUDfBfVw/5odkR/+Ma07/k29S/5h1Vv+ceFn/
ontc/6R/Xf+hhW3/v7Gm/9TLw//d19D/4tzV/+ji
3P/x7er/+Pfz//z79//9/Pn//fz5//38+f/9/Pn/
/Pz4//36+P/8+/j//Pv3//z59//8+vb/+vn1//r4
9P/69vP/1MrB/0xEPv+HY0f/oHdU/6B2VP+Rakv/
dFI3/wcHB4gHBwdpBwcHRgcHBykHBwcUBwcHBgAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcH
BwMHBwcKkW1P/7aRb//JpYH/y6aD/8GihP/DoYL/
yaWB/8ejgP/FoX7/wZ59/76aev+6l3f/tpN0/7KP
b/+ui2v/q4dn/6eDZP+if1//nnxb/5p3WP+SblDw
iGZH139fQsV2Vjmqak0zlGVIL3xfQy1mUzsoTD4s
HjIHBwcbBwcHGQcHBxcHBwcVBwcHEwcHBxIHBwcQ
BwcHDwcHBw0HBwcMBwcHCgcHBwkHBwcHBwcHBwcH
BwUHBwcEBwcHAwcHBwIHBwcBBwcHAQAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAHBwcBBwcHAQcHBwMHBwcEBwcHBQcHBwcHBwcJ
BwcHCwcHBw0HBwcQLyIXHlQ5JUddQCl1Zkcun3FQ
NsZ9WjzrhmFE/4pnSf+Qa03/lG9Q/5hzVP+edlf/
oXpZ/6WLd//Fua3/1czF/93Xz//h29T/5+Lc//Ds
6v/49/P/+/r3//z7+P/8+/f//Pn3//v69v/7+fX/
+vn0//r48//TycH/Uj4w/4hlR/+heFX/oXhV/5Fq
Sv9zUTf+BwcHewcHB14HBwc+BwcHJAcHBxEHBwcF
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BwcHAQcHBwZ/Wz3/mXVW/6yHZv+vi2n/ropq/6uI
Z/+phGX/pYJh/6F9Xv+ceVv/lnNU9olmSdeEYUTN
eFY8q3BRNZxmSDF8YkUua1Q7KE1INSQ7BwcHHAcH
BxkHBwcXBwcHFgcHBxMHBwcSBwcHEAcHBw8HBwcN
BwcHDAcHBwoHBwcJBwcHBwcHBwcHBwcGBwcHBQcH
BwQHBwcDBwcHAgcHBwEHBwcBBwcHAQAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcH
BwEHBwcBBwcHAwcHBwQHBwcFBwcHBwcHBwkHBwcL
BwcHDQcHBxA5JxokVTslTV0/KXVlRi+kclA2y3tY
O/CDX0H/iGRF/4xoSf+Sa0z/lnFQ/5pyU/+cd1X/
qZJ//8i9sf/TzMX/2tPM/93Wzf/j39f/7+zn//f1
8P/6+PT/+vjz/9HKv/9nTjj/j2pM/6N5Vv+hd1T/
kGlK/21MM/MHBwdpBwcHUAcHBzQHBwceBwcHDgcH
BwQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAHBwcBBwcHA2RHLx5xUDVTdFQ3iHdXOaR1VTig
aUsyeWdJMXFVPClMUDomQwcHBxwHBwcaBwcHGAcH
BxYHBwcUBwcHEwcHBxAHBwcPBwcHDQcHBwwHBwcK
BwcHCQcHBwgHBwcHBwcHBgcHBwUHBwcEBwcHBAcH
BwMHBwcCBwcHAQcHBwEAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwcHAQcH
BwEHBwcDBwcHBAcHBwUHBwcHBwcHCQcHBwsHBwcN
BwcHEEAtHSlVPCVSXT4oemVFLaVwUTXQe1g69YFd
P/+GYUP/imVH/5BrSv+Tbk3/mHFQ/5h1Vv+mkX3/
wraq/8zDuP/Px7z/sKKS/5BsTv+edlX/o3pX/6B2
Vv+PZ0n/Z0gv5QcHB1IHBwc+BwcHKAcHBxYHBwcK
BwcHAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAHBwcBBwcHAgcHBwQHBwcHBwcHCgcH
BwwHBwcNBwcHDQcHBw0HBwcMBwcHCwcHBwoHBwcI
BwcHBwcHBwYHBwcFBwcHBAcHBwQHBwcDBwcHAgcH
BwEHBwcBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAHBwcBBwcHAQcH
BwMHBwcEBwcHBgcHBwcHBwcKBwcHDAcHBw4HBwcQ
RTAfL1Y8JlhdPyiAZEYup3FPNdN6WDr6f1w+/4Vf
Qv+IY0T/jmdI/5JrS/+Wb07/mXBQ/5lzUP+ZcVD/
k2xM/4FcPv9cPifOBwcHNwcHBykHBwcaBwcHDwcH
BwcHBwcBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAABwcHAQcHBwEHBwcB
BwcHAgcHBwMHBwcDBwcHAwcHBwIHBwcBBwcHAQAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAABwcHAQcHBwEHBwcCBwcHAwcH
BwQHBwcGBwcHBwcHBwoHBwcMBwcHDgcHBxFGMB4y
VjolW1w9J4NlRi6qcE4003lWOPx+Wjz/f1w9/35a
PP94VDf/ZEQt31c6JZIHBwchBwcHGAcHBw8HBwcI
BwcHBAcHBwEAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAHBwcBBwcHAQcHBwIHBwcDBwcHBAcH
BwYHBwcIBwcHCgcHBwwHBwcOBwcHEUkyITdVOyVb
SzQhRhENCxsHBwcXBwcHFAcHBxAHBwcMBwcHBwcH
BwQHBwcBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAcHBwEHBwcBBwcHAgcHBwMHBwcEBwcHBgcH
BwcHBwcIBwcHCAcHBwgHBwcHBwcHBQcHBwQHBwcC
BwcHAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAcHBwEHBwcBBwcHAQAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAA////////////////
////////////////////////////////////////
////////////////////////////////////////
///////////////////////////////////////8
AAAAA////////////+AAAAAAAAAA////////4AAA
AAAAAAAAAAB//////4AAAAAAAAAAAAAAAB////8A
AAAAAAAAAAAAAAAAD///AAAAAAAAAAAAAAAAAAD/
/gAAAAAAAAAAAAAAAAAAP/4AAAAAAAAAAAAAAAAA
AB/+AAAAAAAAAAAAAAAAAAAf/gAAAAAAAAAAAAAA
AAAAH/4AAAAAAAAAAAAAAAAAAB/+AAAAAAAAAAAA
AAAAAAAf/gAAAAAAAAAAAAAAAAAAH/4AAAAAAAAA
AAAAAAAAAB/+AAAAAAAAAAAAAAAAAAAf/gAAAAAA
AAAAAAAAAAAAH/4AAAAAAAAAAAAAAAAAAB/+AAAA
AAAAAAAAAAAAAAAf/gAAAAAAAAAAAAAAAAAAH/4A
AAAAAAAAAAAAAAAAAB/+AAAAAAAAAAAAAAAAAAAf
/gAAAAAAAAAAAAAAAAAAH/4AAAAAAAAAAAAAAAAA
AA/+AAAAAAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAA
AAAAB/4AAAAAAAAAAAAAAAAAAAf+AAAAAAAAAAAA
AAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAA
AAAAAAAAAAf+AAAAAAAAAAAAAAAAAAAH/gAAAAAA
AAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAAf+AAAA
AAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4A
AAAAAAAAAAAAAAAAAAf+AAAAAAAAAAAAAAAAAAAH
/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAA
AAf+AAAAAAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAA
AAAAB/4AAAAAAAAAAAAAAAAAAAf+AAAAAAAAAAAA
AAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAA
AAAAAAAAAAf+AAAAAAAAAAAAAAAAAAAH/gAAAAAA
AAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAAf+AAAA
AAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4A
AAAAAAAAAAAAAAAAAAf+AAAAAAAAAAAAAAAAAAAH
/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAA
AAf+AAAAAAAAAAAAAAAAAAAH/gAAAAAAAAAAAAAA
AAAAB/4AAAAAAAAAAAAAAAAAAAf+AAAAAAAAAAAA
AAAAAAAH/gAAAAAAAAAAAAAAAAAAB/4AAAAAAAAA
AAAAAAAAAAf+AAAAAAAAAAAAAAAAAAAH/gAAAAAA
AAAAAAAAAAAAB/4AAAAAAAAAAAAAAAAAAAf+AAAA
AAAAAAAAAAAAAAAH+AAAAAAAAAAAAAAAAAAAB/gA
AAAAAAAAAAAAAAAAAAf4AAAAAAAAAAAAAAAAAAAH
+AAAAAAAAAAAAAAAAAAAB/gAAAAAAAAAAAAAAAAA
AAf4AAAAAAAAAAAAAAAAAAAf+AAAAAAAAAAAAAAA
AAAAP/gAAAAAAAAAAAAAAAAAAD/4AAAAAAAAAAAA
AAAAAAA/+AAAAAAAAAAAAAAAAAAAP/gAAAAAAAAA
AAAAAAAAAD/4AAAAAAAAAAAAAAAAAAA/+AAAAAAA
AAAAAAAAAAAAP/gAAAAAAAAAAAAAAAAAAD/4AAAA
AAAAAAAAAAAAAAA/+AAAAAAAAAAAAAAAAAAAP/gA
AAAAAAAAAAAAAAAAAD/4AAAAAAAAAAAAAAAAAAA/
+AAAAAAAAAAAAAAAAAAAP/gAAAAAAAAAAAAAAAAA
AD/4AAAAAAAAAAAAAAAAAAA/+AAAAAAAAAAAAAAA
AAAAP/gAAAAAAAAAAAAAAAAAAD/4AAAAAAAAAAAA
AAAAAAA/+AAAAAAAAAAAAAAAAAAAP/gAAAAAAAAA
AAAAAAAAAD/4AAAAAAAAAAAAAAAAAAA/+AAAAAAA
AAAAAAAAAAAAP/gAAAAAAAAAAAAAAAAAAD/4AAAA
AAAAAAAAAAAAAAA/+AAAAAAAAAAAAAAAAAAAP/gA
AAAAAAAAAAAAAAAAAD/4AAAAAAAAAAAAAAAAAAA/
+AAAAAAAAAAAAAAAAAAAP/gAAAAAAAAAAAAAAAAA
AD/4AAAAAAAAAAAAAAAAAAA/+AAAAAAAAAAAAAAA
AAAAP/gAAAAAAAAAAAAAAAAAAD/4AAAAAAAAAAAA
AAAAAAA/+AAAAAAAAAAAAAAAAAAAP/8AAAAAAAAA
AAAAAAAAAD//AAAAAAAAAAAAAAAAAAB//wAAAAAA
AAAAAAAAAAAAf/8AAAAAAAAAAAAAAAAAAH//AAAA
AAAAAAAAAAAAAAB//wAAAAAAAAAAAAAAAAAAf/8A
AAAAAAAAAAAAAAAAAH//AAAAAAAAAAAAAAAAAAB/
/wAAAAAAAB/4AAAAAAAAf/8AAAAAAB///+AAAAAA
AH//AAAAAH//////gAAAAAB//4AAAf////////4A
AAAAf//gB///////////8AAAAH//////////////
///AAAD//////////////////wAB////////////
///////+P///////////////////////////////
//////////////////////////////////8=
'''

def decode_icon(base64code):
   # generating the icon
   import base64

   byte = base64code.replace('\n',"")
   
  
   decodeit = open('icon.ico', 'wb')
   decodeit.write(base64.b64decode((byte)))
   decodeit.close()

# Defining TextEditor Class
class TextEditor:

  # Defining Constructor
  def __init__(self,root):
    #decoding the icon
    decode_icon(encoded_icon)
    # Assigning root
    self.root = root
    # Title of the window
    self.root.title("light_notepad 1.0.4")
    # Window Geometry
    self.root.geometry("600x400")
    # setting up titlebar icon
    try:
    # you can change the icon from changing icon.ico file
      root.iconbitmap(getcwd()+"/icon.ico")
    except:
    # if an exception occurs
      messagebox.showerror("","icon.ico file not found")
    # Initializing filename
    self.filename = None
    # Declaring Title variable
    self.title = StringVar()
    # Declaring Status variable
    self.status = StringVar()

    # Creating Titlebar 
    self.titlebar = Label(self.root,textvariable=self.title,fg=titlebar_fg,bg=titlebar_bg,font=titlebar_font,bd=titlebar_bd,relief=SOLID)
    # Packing Titlebar to root window
    self.titlebar.pack(side=TOP,fill=BOTH)
    # Calling Settitle Function
    self.settitle()

    # Creating Statusbar
    self.statusbar = Label(self.root,textvariable=self.status,fg=statusbar_fg,bg=statusbar_bg,font=statusbar_font,bd=statusbar_bd,relief=GROOVE)

    # Creating Menubar
    self.menubar = Menu(self.root,font=menubar_font,activebackground=menubar_activebackground)
    # Configuring menubar on root window
    self.root.config(menu=self.menubar)

    # Creating File Menu
    self.filemenu = Menu(self.menubar,fg=menuspecs_fg,bg=menuspecs_bg,font=menuspecs_font,activebackground=menuspecs_activebackground,tearoff=0)
    # Adding New file Command
    self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
    # Adding Open file Command
    self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
    # Adding Save File Command
    self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
    # Adding Save As file Command
    self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
    # Adding Seprator
    self.filemenu.add_separator()
    # Adding Exit window Command
    self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
    # Cascading filemenu to menubar
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    # Creating Edit Menu
    self.editmenu = Menu(self.menubar,fg=menuspecs_fg,bg=menuspecs_bg,font=menuspecs_font,activebackground=menuspecs_activebackground,tearoff=0)
    # Adding Cut text Command
    self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
    # Adding Copy text Command
    self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
    # Adding Paste text command
    self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
    # Adding Seprator
    self.editmenu.add_separator()
    # Adding Undo text Command
    self.editmenu.add_command(label="Undo",accelerator="Ctrl+U",command=self.undo)
    # Cascading editmenu to menubar
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    # Creating Upload Menu
    self.upload = Menu(self.menubar,fg=menuspecs_fg,bg=menuspecs_bg,font=menuspecs_font,activebackground=menuspecs_activebackground,tearoff=0)
    # Adding licence Command
    self.upload.add_command(label="Upload-to-0x0.st",command=self.uploadf)
    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Upload", menu=self.upload)

    # Creating Other Menu
    self.helpmenu = Menu(self.menubar,fg=menuspecs_fg,bg=menuspecs_bg,font=menuspecs_font,activebackground=menuspecs_activebackground,tearoff=0)
    # Adding About Command
    self.helpmenu.add_command(label="About-light",command=self.infoabout)
    # Adding user-manuals Command
    self.helpmenu.add_command(label="Configuration",command=self.configure)
    # Adding user-manuals Command
    self.helpmenu.add_command(label="Restart",command=self.restart_program)
    # Adding licence Command
    self.helpmenu.add_command(label="License",command=self.license)
    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Other", menu=self.helpmenu)

    # Creating Scrollbars
    scrol_x = Scrollbar(self.root,orient=HORIZONTAL)
    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    # Creating Text Area
    self.txtarea = Text(self.root,wrap="none",fg=txtarea_fg,bg=txtarea_bg,insertbackground=txtarea_cursor_color,yscrollcommand=scrol_y.set,xscrollcommand=scrol_x.set,font=txtarea_font,state="normal",relief=GROOVE)
    # Packing scrollbars to root window
    scrol_x.pack(side=BOTTOM,fill=X)
    scrol_y.pack(side=RIGHT,fill=Y)
    # Adding Scrollbars to text area
    scrol_x.config(command=self.txtarea.xview)
    scrol_y.config(command=self.txtarea.yview)
    # Packing Text Area to root window
    self.txtarea.pack(fill=BOTH,expand=1)

    # Calling shortcuts function
    self.shortcuts()

  # Defining settitle function
  def settitle(self):
    # Checking if Filename is not None
    if self.filename:
      # Updating Title as filename
      self.title.set(self.filename)
    else:
      # Updating Title as Untitled
      self.title.set("Untitled")

  # Defining New file Function
  def newfile(self,*args):
    # Clearing the Text Area
    self.txtarea.delete("1.0",END)
    # Updating filename as None
    self.filename = None
    # Calling settitle function
    self.settitle()
    # updating status
    self.status.set("New File Created")

  # Defining Open File function
  def openfile(self,*args):
    # Exception handling
    try:
      # Asking for file to open
      self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      # checking if filename not none
      if self.filename:
        # opening file in readmode
        infile = open(self.filename,"r")
        # Clearing text area
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing the file  
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save File function
  def savefile(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Reading the data from text area
        data = self.txtarea.get("1.0",END)
        # opening File in write mode
        outfile = open(self.filename,"w")
        # Writing Data into file
        outfile.write(data)
        # Closing File
        outfile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Saved Successfully")
      else:
        self.saveasfile()
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save As File function
  def saveasfile(self,*args):
    # Exception handling
    try:
      # Asking for file name and type to save
      untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      # Reading the data from text area
      data = self.txtarea.get("1.0",END)
      # opening File in write mode
      outfile = open(untitledfile,"w")
      # Writing Data into file
      outfile.write(data)
      # Closing File
      outfile.close()
      # Updating filename as Untitled
      self.filename = untitledfile
      # Calling Set title
      self.settitle()
      # Updating Status
      self.status.set("Saved Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Exit function
  def exit(self,*args):
    op = messagebox.askyesno("","  Are you sure ?")
    if op>0:
      self.root.destroy()
    else:
      return

  # Defining Cut function
  def paste(self,*args):
    self.txtarea.event_generate("<<Paste>>")

  # Defining Cut function
  def cut(self,*args):
    self.txtarea.event_generate("<<Cut>>")

  # Defining Copy function
  def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")

  # Defining Undo function
  def undo(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # opening File in read mode
        infile = open(self.filename,"r")
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing File
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
      else:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # Updating filename as None
        self.filename = None
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining About function
  def infoabout(self):
    messagebox.showinfo("About light Text Editor","A Simple light weight Text Editor Created using Python.")

  # Defining shortcuts function
  def shortcuts(self):
    # Binding Ctrl+n to newfile function
    self.txtarea.bind("<Control-n>",self.newfile)
    # Binding Ctrl+o to openfile function
    self.txtarea.bind("<Control-o>",self.openfile)
    # Binding Ctrl+s to savefile function
    self.txtarea.bind("<Control-s>",self.savefile)
    # Binding Ctrl+a to saveasfile function
    self.txtarea.bind("<Control-a>",self.saveasfile)
    # Binding Ctrl+e to exit function
    self.txtarea.bind("<Control-e>",self.exit)
    # Binding Ctrl+x to cut function
    self.txtarea.bind("<Control-x>",self.cut)
    # Binding Ctrl+c to copy function
    self.txtarea.bind("<Control-c>",self.copy)
    # Binding Ctrl+u to undo function
    self.txtarea.bind("<Control-u>",self.undo)
    # Binding Ctrl+l to upload function
    self.txtarea.bind("<Control-l>",self.uploadf)
  
  def restart_program(self):
    #Restarts the current program.
    #Note: this function does not return. Any cleanup action (like
    #saving data) must be done before calling this function."""
    python = executable
    execl(python, python, * argv)
  
  def configure(self):
    try:
      # Asking for file to open
      self.filename = argv[0]
      # checking if filename not none
      if self.filename:
        # opening file in readmode
        infile = open(self.filename,"r")
        # Clearing text area
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing the file  
        infile.close()
        # Calling Set title
        self.title.set("configure the specsifictions of the program")
        # Updating Status
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  def license(self):
    try:
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in LICENSE:
          self.txtarea.insert(END,line)
        # Calling Set title
        self.title.set("license")
        # Updating Status
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  def uploadf(self):
    # Reading the data from text area
    data = self.txtarea.get("1.0",END)
    # opening File in write
    outfile = open("untitledfile","w")
    # Writing Data into file
    outfile.write(data)
    # Closing File
    outfile.close()
    try:
      from requests import post
    except:
      messagebox.showerror("Exception","requests module not found !")
    url = uploading_destination
    x = open("untitledfile", "rb")
    files = {"file": x}
    r = post(url, files=files)
    print(r.text)
    self.title.set(r.text.replace("\n",""))
    messagebox.showinfo("file-destination",r.text.replace("\n",""))
    x.close()
    if path.isfile("untitledfile"):
      remove("untitledfile")
    else:
      messagebox.showinfo("this is not file","something went wrong I think .d")

# Creating TK Container
root = Tk()
#Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()
