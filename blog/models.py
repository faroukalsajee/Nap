from django.db import models

# New imports added for ParentalKey, Orderable, InlinePanel, ImageChooserPanel

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from wagtail.snippets.models import register_snippet




@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    class BlogPage(Page):
        date = models.DateField("Post date")
        intro = models.CharField(max_length=250)
        body = RichTextField(blank=True)

        def main_image(self):
            gallery_item = self.gallery_images.first()
            if gallery_item:
                return gallery_item.image
            else:
                return None

        search_fields = Page.search_fields + [
            index.SearchField('intro'),
            index.SearchField('body'),
        ]

        content_panels = Page.content_panels + [
            FieldPanel('date'),
            FieldPanel('intro'),
            FieldPanel('body', classname="full"),
            InlinePanel('gallery_images', label="Gallery images"),
        ]

        class BlogPageGalleryImage(Orderable):
            page = ParentalKey(Page, on_delete=models.CASCADE, related_name='gallery_images')
            image = models.ForeignKey(
                'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
            )
            caption = models.CharField(blank=True, max_length=250)

            panels = [
                ImageChooserPanel('image'),
                FieldPanel('caption'),
            ]