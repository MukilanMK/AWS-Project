"""Seed a sample biography post about Dr APJ Abdul Kalam."""
from app import create_app, db
from app.models import Post, Tag


def main():
    app = create_app()
    with app.app_context():
        title = "Dr APJ Abdul Kalam — A Brief Biography"
        if Post.query.filter_by(title=title).first():
            print("Sample post already exists")
            return
        body = (
            "<p>Avul Pakir Jainulabdeen Abdul Kalam (1931–2015) was an Indian aerospace scientist and statesman who served as the 11th President of India from 2002 to 2007.</p>"
            "<p>Born in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering, worked at DRDO and ISRO, and played prominent roles in the development of India's satellite launch and missile programs.</p>"
            "<p>Kalam emphasized education, research, and mentorship; after his presidency he continued lecturing and working with students until his death in 2015.</p>"
        )
        post = Post(title=title, body=body)
        tag = Tag.query.filter_by(name="Biography").first()
        if not tag:
            tag = Tag(name="Biography")
        post.tags.append(tag)
        db.session.add(post)
        db.session.commit()
        print("Sample post created")


if __name__ == "__main__":
    main()
