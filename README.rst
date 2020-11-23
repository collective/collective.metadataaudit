.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.


========================
collective.metadataaudit
========================

``collective.metaaaudit`` logs metadata changes to Plone content objects transparently
(for all content types). This add-on in in particular useful when you have to answer
the question "who was doing what and when".

Install and use this add-on with care. In particular ensure that its usage is compliant
with your local privacy and data-protection legislation.

Features
--------

- logs all metadata changes (create and edit operations) for all Plone content types 
  (Dexterity content-types only)


Installation
------------

Install collective.metadataaudit by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.metadataaudit


and then running ``bin/buildout``

Usage
-----

- Use the ``Logging`` entry from the Plone toolbar


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.metadataaudit/issues
- Source Code: https://github.com/collective/collective.metadataaudit


License
-------

The project is licensed under the GPLv2.

Author
------

Andreas Jung (info@zopyx.com)
