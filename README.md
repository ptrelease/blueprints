blueprints
==========

examples of how to create and use python blueprints

install requirements by typing:

  pip install -r requirements.txt
  
make the run script executable by typing:
  
  chmod a+x run.py
  
then type this to run:

  ./run.py
  

how it works
============

The blueprint is called try_blueprint.py.  Its registered in the apps init.py.  Calling then route to the blueprint renders the associated template.  The route at the landing page is not in a blueprint (see server.py).
