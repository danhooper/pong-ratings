# pong-ratings

pong-ratings is a ping pong handicapper.

## Installation

### Vagrant
To install a local version of the site use [Vagrant](http://www.vagrantup.com/)

```bash
vagrant up
```

After provisioning is complete, the site should now be accessible on
[http://localhost:11080/pong_ratings](http://localhost:11080/pong_ratings)

### Deployment
Refer to the [vagrant provision script](vagrant/pong_provision.sh) for
installation steps.  The
[local/supervisor/pong_ratings.conf](local/supervisor/pong_ratings.conf) and
[local/nginx/pong_ratings.conf](local/nginx/pong_ratings.conf) files will need
to be modified per your deployment directory.
